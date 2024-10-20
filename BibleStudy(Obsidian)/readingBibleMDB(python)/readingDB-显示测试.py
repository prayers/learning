import sqlite3
import openpyxl
import os


def read_bible_id_table(db_file):
    """
    读取 BibleID 表的所有内容并打印

    Args:
        db_file: 数据库文件名
    """

    try:
        # 连接数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行查询
        cursor.execute("SELECT * FROM BibleID")

        # 获取所有结果
        rows = cursor.fetchall()

        # 打印表头
        print("SN\tKindSN\tChapterNumber\tNewOrOld\tPinYin\tShortName\tFullName")

        # 打印数据
        for row in rows:
            print("\t".join(str(col) for col in row))

    except sqlite3.Error as e:
        print(f"Error {e}")
    finally:
        if conn:
            conn.close()


def get_fullname_by_sn(db_file, sn):
    """
    根据 SN 从 BibleID 表中读取对应的 FULLNAME

    Args:
        db_file: 数据库文件名
        sn: SN 值
    """

    try:
        # 连接数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行查询
        cursor.execute("SELECT FullName FROM BibleID WHERE SN=?", (sn,))

        # 获取结果
        result = cursor.fetchone()

        # fullname
        fullname = result[0]

        if result:
            print(f"FULLNAME: {fullname}")
        else:
            print(f"未找到 SN 为 {sn} 的记录")

        return fullname

    except sqlite3.Error as e:
        print(f"Error {e}")
    finally:
        if conn:
            conn.close()


def query_bible_range(db_file, volume_sn, start_chapter_sn, start_verse_sn, end_chapter_sn, end_verse_sn):
    """
    从 SQLite 数据库中查询指定范围内的经文内容

    Args:
        db_file: 数据库文件名
        volume_sn: 经卷序号
        start_chapter_sn: 开始章节序号
        start_verse_sn: 开始节数序号
        end_chapter_sn: 结束章节序号
        end_verse_sn: 结束节数序号
    """

    try:
        # 连接数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 构建 SQL 查询语句
        if start_chapter_sn == end_chapter_sn:
            sql = f"""
                SELECT Lection
                FROM Bible
                WHERE VolumeSN = ?
                AND (VolumeSN = ? AND ChapterSN = ? AND VerseSN = ?)
                OR (VolumeSN = ? AND ChapterSN > ? AND ChapterSN < ?)
                OR (VolumeSN = ? AND ChapterSN = ? AND VerseSN <= ?)
                ORDER BY ChapterSN, VerseSN
            """
        elif start_chapter_sn < end_chapter_sn:
            sql = f"""
                SELECT Lection
                FROM Bible
                WHERE VolumeSN = ?
                AND (VolumeSN = ? AND ChapterSN = ? AND VerseSN >= ?)
                OR (VolumeSN = ? AND ChapterSN > ? AND ChapterSN < ?)
                OR (VolumeSN = ? AND ChapterSN = ? AND VerseSN <= ?)
                ORDER BY ChapterSN, VerseSN
            """
        else:
            raise ("章节填写错误")

        # 执行查询
        cursor.execute(sql, (volume_sn, volume_sn, start_chapter_sn, start_verse_sn, volume_sn,
                       start_chapter_sn, end_chapter_sn, volume_sn, end_chapter_sn, end_verse_sn))
        results = cursor.fetchall()

        # 打印查询结果
        for result in results:
            print(result[0])

    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        # 关闭数据库连接
        if conn:
            conn.cursor()


def query_bible(db_file, volume_sn, chapter_sn, verse_sn):
    """
    从 SQLite 数据库中查询经文内容

    Args:
        db_file: 数据库文件名
        volume_sn: 经卷序号
        chapter_sn: 章节序号
        verse_sn: 节数序号
    """

    try:
        # 连接数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 构建 SQL 查询语句
        sql = f"SELECT Lection FROM Bible WHERE VolumeSN=? AND ChapterSN=? AND VerseSN=?"

        # 执行查询
        cursor.execute(sql, (volume_sn, chapter_sn, verse_sn))
        result = cursor.fetchone()

        if result:
            print(result[0])
        else:
            print("未找到对应的经文")

    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        # 关闭数据库连接
        if conn:
            conn.close()


def export_bible_to_excel(db_file, table_name, columns_in_db):
    """
    将 SQLite 数据库中的圣经经文数据导出到 Excel 文件

    Args:
        db_file: 数据库文件名
        table_name: 表名
        output_file: 输出 Excel 文件名
        columns: 字段列表，对应 Excel 的列名
    """

    try:
        # 连接数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 查询所有经文信息
        sql = f"SELECT {', '.join(columns_in_db)} FROM {table_name}"
        cursor.execute(sql)

        # 打印查询内容
        for result in cursor:
            print(result[0])
            print(result[1])
            print(result[2])
            print(result[3])

    except Exception as e:
        print(f"导出数据失败: {e}")
    finally:
        # 关闭数据库连接
        if conn:
            conn.close()


def export_bible_to_markdown(db_file, output_dir):
    """
    将 Bible 表中的数据按照 VolumeSN 分割成 Markdown 文件

    Args:
        db_file: 数据库文件名
        output_dir: 输出目录
    """

    try:
        # 连接数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 查询所有经文信息
        cursor.execute(
            "SELECT VolumeSN, ChapterSN, VerseSN, Lection FROM Bible")

        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)

        # 按照 VolumeSN 分组并生成 Markdown 文件
        current_volume = None
        current_chapter = None

        for row in cursor:
            volume_sn, chapter_sn, verse_sn, lection = row

            if volume_sn != current_volume:
                # 新建文件
                if current_volume is not None:
                    f.close()
                current_volume = volume_sn
                fullname = get_fullname_by_sn(db_file, current_volume)
                with open(os.path.join(output_dir, f"{current_volume:02d}_{fullname}.md"), 'w', encoding='utf-8') as f:
                    f.write(f"# {fullname}\n")
                f.close()
            with open(os.path.join(output_dir, f"{current_volume:02d}_{fullname}.md"), 'a+', encoding='utf-8') as f:
                # 写入 Markdown 内容
                if current_chapter != chapter_sn:
                    current_chapter = chapter_sn
                    f.write(f"## Chapter {chapter_sn}\n")
                f.write(f"- {verse_sn} {lection}\n")

    except sqlite3.Error as e:
        print(f"导出数据失败: {e}")
    finally:
        if conn:
            conn.close()


# 使用示例
db_file = 'bible_简体中文和合本.db'
table_name = 'Bible'
columns_in_db = ['VolumeSN', 'ChapterSN', 'VerseSN', 'Lection']

# export_bible_to_excel(db_file, table_name, columns_in_db)

# 根据章节读取经文
volume_sn = 1
chapter_sn = 1
verse_sn = 1

query_bible(db_file, volume_sn, chapter_sn, verse_sn)

# 读取连续经文
start_chapter_sn = 1
start_verse_sn = 1
end_chapter_sn = 1
end_verse_sn = 3

query_bible_range(db_file, volume_sn, start_chapter_sn,
                  start_verse_sn, end_chapter_sn, end_verse_sn)

# 查询BibleID表
# read_bible_id_table(db_file) # 读取BibleID表的全部内容
fullname = get_fullname_by_sn(db_file, 66)
print(fullname)

# 输出markdown
output_dir = 'bible_markdown'

# export_bible_to_markdown(db_file, output_dir)
