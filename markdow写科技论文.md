# 这是题目
作者名字[^1]

[^1]: 这是脚注

## 1. Introduction

This is $y^2=x+b$

is review is provided a detailed overview of the synthesis, properties and applications of nanoparticles (NPs) exist in different forms. NPs are tiny materials having size ranges from 1 to 100 nm[@KHAN2019908], Their reactivity, toughness and other properties are also dependent on their unique size, shape and structure. Due to these characteristics, they are suitable candidates for various commercial and domestic applications, which include catalysis, imaging, medical applications[@THIHER2021109737], energy-based research, and environmental applications. Heavy metal NPs of lead, mercury and tin are reported to be so rigid and stable that their degradation is not easily achievable, which can lead to many environmental toxicities[@SARKAR2022737330].


'''
pandoc -s --bibliography mybib1.bib --bibliography mybib2.bib --citeproc --csl chinese-gb7714-2015-numeric.csl --metadata reference-section-title="参考文献" --metadata link-citations=true markdow写科技论文.md -o markdow写科技论文.docx
'''

## 2. 下载安装pandoc
https://pandoc.org/