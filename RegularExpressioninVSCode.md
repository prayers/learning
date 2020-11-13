# Use regular expressions in Visual Studio
Visual Studio uses .NET regular expressions to find and replace text.

<table>

<thead>

<tr>

<th>Purpose</th>

<th>Expression</th>

<th>Example</th>

</tr>

</thead>

<tbody>

<tr>

<td>Match any single character (except a line break). For more information, see [Any character](/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#any-character-).</td>

<td>.</td>

<td>`a.o` matches "aro" in "around" and "abo" in "about" but not "acro" in "across"</td>

</tr>

<tr>

<td>Match zero or more occurrences of the preceding expression (match as many characters as possible). For more information, see [Match zero or more times](/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions#match-zero-or-more-times-).</td>

<td>*</td>

<td>`a*r` matches "r" in "rack", "ar" in "ark", and "aar" in "aardvark"</td>

</tr>

<tr>

<td>Match any character zero or more times.</td>

<td>.*</td>

<td>`c.*e` matches "cke" in "racket", "comme" in "comment", and "code" in "code"</td>

</tr>

<tr>

<td>Match one or more occurrences of the preceding expression (match as many characters as possible). For more information, see [Match one or more times](/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions#match-one-or-more-times-).</td>

<td>+</td>

<td>`e+d` matches "eed" in "feeder" and "ed" in "faded"</td>

</tr>

<tr>

<td>Match any character one or more times.</td>

<td>.+</td>

<td>`e.+e` matches "eede" in "feeder" but finds no matches in "feed"</td>

</tr>

<tr>

<td>Match zero or more occurrences of the preceding expression (match as few characters as possible). For more information, see [Match zero or more times (lazy match)](/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions#match-zero-or-more-times-lazy-match-).</td>

<td>*?</td>

<td>`\w*?d` matches "fad" and "ed" in "faded" but not the entire word "faded" due to the lazy match</td>

</tr>

<tr>

<td>Match one or more occurrences of the preceding expression (match as few characters as possible). For more information, see [Match one or more times (lazy match)](/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions#match-one-or-more-times-lazy-match-).</td>

<td>+?</td>

<td>`e\w+?` matches "ee" in "asleep" and "ed" in "faded" but finds no matches in "fade"</td>

</tr>

<tr>

<td>Anchor the match string to the [beginning of a line or string](/en-us/dotnet/standard/base-types/anchors-in-regular-expressions#start-of-string-or-line-)</td>

<td>^</td>

<td>`^car` matches the word "car" only when it appears at the beginning of a line</td>

</tr>

<tr>

<td>Anchor the match string to the [end of a line](/en-us/dotnet/standard/base-types/anchors-in-regular-expressions#end-of-string-or-line-)</td>

<td>\r?$</td>

<td>`car\r?<td matches "car" only when it appears at the end of a line</td>

</tr>

<tr>

<td>Anchor the match string to the end of the file</td>

<td>$</td>

<td>`car<td matches "car" only when it appears at the end of the file</td>

</tr>

<tr>

<td>Match any single character in a set</td>

<td>[abc]</td>

<td>`b[abc]` matches "ba", "bb", and "bc"</td>

</tr>

<tr>

<td>Match any character in a range of characters</td>

<td>[a-f]</td>

<td>`be[n-t]` matches "bet" in "between", "ben" in "beneath", and "bes" in "beside", but finds no matches in "below"</td>

</tr>

<tr>

<td>Capture and implicitly number the expression contained within parenthesis</td>

<td>()</td>

<td>`([a-z])X\1` matches "aXa"and "bXb", but not "aXb". "\1" refers to the first expression group "[a-z]". For more information, see [Capture groups and replacement patterns](#capture-groups-and-replacement-patterns).</td>

</tr>

<tr>

<td>Invalidate a match</td>

<td>(?!abc)</td>

<td>`real(?!ity)` matches "real" in "realty" and "really" but not in "reality." It also finds the second "real" (but not the first "real") in "realityreal".</td>

</tr>

<tr>

<td>Match any character that is not in a given set of characters. For more information, see [Negative character group](/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#negative-character-group-).</td>

<td>[^abc]</td>

<td>`be[^n-t]` matches "bef" in "before", "beh" in "behind", and "bel" in "below", but finds no matches in "beneath"</td>

</tr>

<tr>

<td>Match either the expression before or the one after the symbol</td>

<td>|</td>

<td>`(sponge|mud) bath` matches "sponge bath" and "mud bath"</td>

</tr>

<tr>

<td>[Escape the character](/en-us/dotnet/standard/base-types/character-escapes-in-regular-expressions) following the backslash</td>

<td>\</td>

<td>`\^` matches the character ^</td>

</tr>

<tr>

<td>Specify the number of occurrences of the preceding character or group. For more information, see [Match exactly n times](/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions#match-exactly-n-times-n).</td>

<td>{n}, where 'n' is the number of occurrences</td>

<td>`x(ab){2}x` matches "xababx"  
`x(ab){2,3}x` matches "xababx" and "xabababx" but not "xababababx"</td>

</tr>

<tr>

<td>[Match text in a Unicode category](/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#unicode-category-or-unicode-block-p). For more information about Unicode character classes, see [Unicode Standard 5.2 Character Properties](http://www.unicode.org/versions/Unicode5.2.0/ch04.pdf).</td>

<td>\p{X}, where "X" is the Unicode number.</td>

<td>`\p{Lu}` matches "T" and "D" in "Thomas Doe"</td>

</tr>

<tr>

<td>[Match a word boundary](/en-us/dotnet/standard/base-types/anchors-in-regular-expressions#word-boundary-b)</td>

<td>\b (Outside a character class `\b` specifies a word boundary, and inside a character class `\b` specifies a backspace.)</td>

<td>`\bin` matches "in" in "inside" but finds no matches in "pinto"</td>

</tr>

<tr>

<td>Match a line break (that is, a carriage return followed by a new line)</td>

<td>\r?\n</td>

<td>`End\r?\nBegin` matches "End" and "Begin" only when "End" is the last string in a line and "Begin" is the first string in the next line</td>

</tr>

<tr>

<td>Match any [word character](/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#word-character-w)</td>

<td>\w</td>

<td>`a\wd` matches "add" and "a1d" but not "a d"</td>

</tr>

<tr>

<td>Match any [whitespace character](/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#whitespace-character-s)</td>

<td>\s</td>

<td>`Public\sInterface` matches the phrase "Public Interface"</td>

</tr>

<tr>

<td>Match any [decimal digit character](/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#decimal-digit-character-d)</td>

<td>\d</td>

<td>`\d` matches "4" and "0" in "wd40"</td>

</tr>

</tbody>

</table>



<div class="TIP">

### Tip

In Windows operating systems, most lines end in "\r\n" (a carriage return followed by a new line). These characters aren't visible but are present in the editor and passed to the .NET regular expression service.

</div>

## Capture groups and replacement patterns
+ within the regular expression: Use \number. For example, \1 in the regular expression (\w+)\s\1 references the first capture group (\w+).

+ in a replacement pattern: Use $number. For example, the grouped regular expression (\d)([a-z]) defines two groups: the first group contains a single decimal digit, and the second group contains a single character between a and z. The expression finds four matches in the following string: 1a 2b 3c 4d. The replacement string z$1 references the first group only ($1), and converts the string to z1 z2 z3 z4.

## Named capture groups
+ within the regular expression: Use \k<name>. For example, \k<repeated> in the regular expression (?<repeated>\w+)\s\k<repeated> references the capture group that's named repeated and whose subexpression is \w+.

+ in a replacement pattern: Use ${name}. For example, ${repeated}.

## Regular expressions quick reference

### **single characters**

| **Use** | **To match any character** |
| --- | --- |
| **[_set_]** | In that set |
| --- | --- |
| **[^_set_]** | Not in that set |
| **[_a–z_]** | In the _a-z_ range |
| **[^_a–z_]** | Not in the a-z range |
| **.** | Any except \n (new line) |
| **\_char_** | Escaped special character |

### **control characters**

| **Use** | **To match** | **Unicode** |
| --- | --- | --- |
| **\t** | Horizontal tab | \u0009 |
| --- | --- | --- |
| **\v** | Vertical tab | \u000B |
| **\b** | Backspace | \u0008 |
| **\e** | Escape | \u001B |
| **\r** | Carriage return | \u000D |
| **\f** | Form feed | \u000C |
| **\n** | New line | \u000A |
| **\a** | Bell (alarm) | \u0007 |
| **\c _char_** | ASCII control character |  |

### **Non-ascii codes**

| **Use** | **To match character with** |
| --- | --- |
| **\_octal_** | 2-3 digit octal character code |
| --- | --- |
| **\x _hex_** | 2-digit hex character code |
| **\u _hex_** | 4-digit hex character code |

### **character classes**

| **Use** | **To match character** |
| --- | --- |
| **\p{_ctgry_}** | In that Unicode category or block |
| --- | --- |
| **\P{_ctgry_}** | Not in that Unicode category or block |
| **\w** | Word character |
| **\W** | Non-word character |
| **\d** | Decimal digit |
| **\D** | Not a decimal digit |
| **\s** | White-space character |
| **\S** | Non-white-space char |

### **quantifiers**

| **Greedy** | **Lazy** | **Matches** |
| --- | --- | --- |
| **\*** | **\*?** | 0 or more times |
| --- | --- | --- |
| **+** | **+?** | 1 or more times |
| **?** | **??** | 0 or 1 time |
| **{_n_}** | **{** _ **n** _ **}?** | Exactly _n_ times |
| **{_n,_}** | **{** _ **n,** _ **}?** | At least _n_ times |
| **{_n,m_}** | **{** _ **n,m** _ **}?** | From _n_ to _m_ times |

### **anchors**

| **Use** | **To specify position** |
| --- | --- |
| **^** | At start of string or line |
| --- | --- |
| **\A** | At start of string |
| **\z** | At end of string |
| **\Z** | At end (or before \n at end) of string |
| **$** | At end (or before \n at end) of string or line |
| **\G** | Where previous match ended |
| **\b** | On word boundary |
| **\B** | Not on word boundary |

### **groups**

| **Use** | **To define** |
| --- | --- |
| **(_exp_)** | Indexed group |
| --- | --- |
| **(?\&lt;_name_\&gt;_exp_)** | Named group |
| **(?\&lt;_name1-name2_\&gt;_exp_)** | Balancing group |
| **(?:_exp_)** | Noncapturing group |
| **(?=_exp_)** | Zero-width positive lookahead |
| **(?!_exp_)** | Zero-width negative lookahead |
| **(?\&lt;=_exp_)** | Zero-width positive lookbehind |
| **(?\&lt;!_exp_)** | Zero-width negative lookbehind |
| **(?\&gt;_exp_)** | Non-backtracking (greedy) |

### **inline options**

| **Option** | **Effect on match** |
| --- | --- |
| **i** | Case-insensitive |
| --- | --- |
| **m** | Multiline mode |
| **n** | Explicit (named) |
| **s** | Single-line mode |
| **x** | Ignore white space |

| **Use** | **To** |
| --- | --- |
| **(?imnsx-imnsx)** | Set or disable the specified options |
| --- | --- |
| **(?imnsx-imnsx:_exp_)** | Set or disable the specified options within the expression |


### **backreferences**

| **Use** | **To match** |
| --- | --- |
| **\_n_** | Indexed group |
| --- | --- |
| **\k\&lt;_name_\&gt;** | Named group |

### **alternation**

| **Use** | **To match** |
| --- | --- |
| **_a_ |_b_** | Either _a_ or _b_ |
| --- | --- |
| **(?(_exp_)

_yes_ | _no_)** | _yes_ if _exp_ is matched  
_no_ if _exp_ isn&#39;t matched |
| **(?(_name_)

_yes_ | _no_)** | _yes_ if _name_ is matched
_no_ if _name_ isn&#39;t matched |

### **substitution**

| **Use** | **To substitute** |
| --- | --- |
| **$_n_** | Substring matched by group number _n_ |
| --- | --- |
| **${_name_}** | Substring matched by group _name_ |
| **$$** | Literal $ character |
| **$&amp;** | Copy of whole match |
| **$`** | Text before the match |
| **$&#39;** | Text after the match |
| **$+** | Last captured group |
| **$\_** | Entire input string |

### **comments**

| **Use** | **To** |
| --- | --- |
| **(?# _comment_)** | Add inline comment |
| --- | --- |
| **#** | Add x-mode comment |

For detailed information and examples, see **http://aka.ms/regex**

To test your regular expressions, see **http://regexlib.com/RETester.aspx**

### **supported unicode categories**

| **Category** | **Description** |
| --- | --- |
| **Lu** | Letter, uppercase |
| --- | --- |
| **LI** | Letter, lowercase |
| **Lt** | Letter, title case |
| **Lm** | Letter, modifier |
| **Lo** | Letter, other |
| **L** | Letter, all |
| **Mn** | Mark, nonspacing combining |
| **Mc** | Mark, spacing combining |
| **Me** | Mark, enclosing combining |
| **M** | Mark, all diacritic |
| **Nd** | Number, decimal digit |
| **Nl** | Number, letterlike |
| **No** | Number, other |
| **N** | Number, all |
| **Pc** | Punctuation, connector |
| **Pd** | Punctuation, dash |
| **Ps** | Punctuation, opening mark |
| **Pe** | Punctuation, closing mark |
| **Pi** | Punctuation, initial quote mark |
| **Pf** | Puntuation, final quote mark |
| **Po** | Punctuation, other |
| **P** | Punctuation, all |
| **Sm** | Symbol, math |
| **Sc** | Symbol, currency |
| **Sk** | Symbol, modifier |
| **So** | Symbol, other |
| **S** | Symbol, all |
| **Zs** | Separator, space |
| **Zl** | Separator, line |
| **Zp** | Separator, paragraph |
| **Z** | Separator, all |
| **Cc** | Control code |
| **Cf** | Format control character |
| **Cs** | Surrogate code point |
| **Co** | Private-use character |
| **Cn** | Unassigned |
| **C** | Control characters, all |

For named character set blocks (e.g., Cyrillic), search for &quot;supported named blocks&quot; in the MSDN Library.

### **regular expression operations**

Class: System.Text.RegularExpressions.Regex

**Pattern matching with Regex objects**

| **To initialize with** | **Use constructor** |
| --- | --- |
| Regular exp | Regex(String) |
| --- | --- |
| + options | Regex(String, RegexOptions) |
| + time-out | Regex(String, RegexOptions,
 TimeSpan) |

**Pattern matching with static methods**

Use an overload of a method below to supply the regular expression and the text you want to search.

### **Finding and replacing matched patterns**

| **To** | **Use method** |
| --- | --- |
| Validate match | Regex.IsMatch |
| --- | --- |
| Retrieve single match | Regex.Match (first)
 Match.NextMatch (next) |
| Retrieve all matches | Regex.Matches |
| Replace match | Regex.Replace |
| Divide text | Regex.Split |
| Handle char escapes | Regex.EscapeRegex.Unescape |

### **Getting info about regular expression patterns**

| **To get** | **Use Regex API** |
| --- | --- |
| Group names | GetGroupNames
 GetGroupNameFromNumber |
| --- | --- |
| Group numbers | GetGroupNumbersGetGroupNumberFromName |
| Expression | ToString |
| Options | Options |
| Time-out | MatchTimeOut |
| Cache size | CacheSize |
| Direction | RightToLeft |