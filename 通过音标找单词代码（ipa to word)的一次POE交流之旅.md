# 情境描述：

在学英文的过程中，经常碰到一些特定的音标搭配，读的时候卡壳了，特别是 弹舌音 t，还有 nt 和 tn 的搭配，tn 搭配如 Clinton，这里 t 不发音，但是该有的 动作一个不能少（舌头要运动到 t 发音的位置就位，就是不发声而已）。nt 搭配譬如 interview，t 也不发音。

适逢笑来老师的 1000h.org，还有学升 app 中提到了 dictionary 的 json 格式，我一看，可以用编程试着找出匹配上述特征的所有单词，加强练习啊。



# 对话式编程过程

以下是和 POE 的对话式编程（黑盒编程），我大概知道用正则表达式来匹配，就是具体细节不知道，但是程序能不能 work，我是知道的。不开玩笑地说，在这里，我的角色是产品经理。



## 第一轮对话

虽然是黑盒式编程，但是结果是正确的：

```
我提问：

我这里有个 json 文件，文件中文本格式如下：{"_id":{"$oid":"60c06f88a54d753a1e7ff079"},"word":"aardvarks","pos_items":[{"type":"noun","pronunciations":[{"region":"uk","audio":"https://dictionary.cambridge.org/media/english/uk_pron/u/uka/uka__/uka____009.mp3","pronunciation":"ˈɑːd.vɑːk"},{"region":"us","audio":"https://dictionary.cambridge.org/media/english/us_pron/u/usa/usad_/usad___007.mp3","pronunciation":"ˈɑːrd.vɑːrk"}],"definitions":[{"definition":"an African mammal with a long nose and large ears that lives underground and eats insects","examples":[]}]}]}
{"_id":{"$oid":"60c06f76a54d753a1e7ff075"},"word":"aah","pos_items":[{"type":"exclamation","pronunciations":[{"region":"uk","audio":"https://dictionary.cambridge.org/media/english/uk_pron/u/uka/uka__/uka____008.mp3","pronunciation":"ɑː"},{"region":"us","audio":"https://dictionary.cambridge.org/media/english/us_pron/u/usa/usad_/usad___006.mp3","pronunciation":"ɑː"}],"definitions":[{"definition":"another spelling of ah","examples":[]}]}]}
{"_id":{"$oid":"60c06fe1a54d753b12266636"},"word":"aback","pos_items":[{"type":"adverb","pronunciations":[{"region":"uk","audio":"https://dictionary.cambridge.org/media/english/uk_pron/u/uka/uka__/uka____011.mp3","pronunciation":"əˈbæk"},{"region":"us","audio":"https://dictionary.cambridge.org/media/english/us_pron/u/usa/usad_/usad___009.mp3","pronunciation":"əˈbæk"}],"definitions":[{"definition":"to be very shocked or surprised","examples":["I was somewhat taken aback by her honesty."]}]}]}
{"_id":{"$oid":"60c06fe9a54d753b12266637"},"word":"abacus","pos_items":[{"type":"noun","pronunciations":[{"region":"uk","audio":"https://dictionary.cambridge.org/media/english/uk_pron/u/uka/uka__/uka____012.mp3","pronunciation":"ˈæb.ə.kəs"},{"region":"us","audio":"https://dictionary.cambridge.org/media/english/us_pron/a/aba/abacu/abacus.mp3","pronunciation":"ˈæb.ə.kəs"}],"definitions":[{"definition":"a square or rectangular frame holding an arrangement of small balls on metal rods or wires, used for counting or for doing calculations","examples":[]},{"definition":"a flat slab (= piece of stone, etc.) at the top of a column","examples":[]}]}]}
{"_id":{"$oid":"60c06f77a54d753a1e7ff076"},"word":"aa","pos_items":[{"type":"noun","pronunciations":[{"region":"uk","audio":"https://dictionary.cambridge.org/media/english/uk_pron/u/uka/uka__/uka____006.mp3","pronunciation":"ˌeɪˈeɪ"},{"region":"us","audio":"https://dictionary.cambridge.org/media/english/us_pron/u/usa/usad_/usad___004.mp3","pronunciation":"ˌeɪˈeɪ"}],"definitions":[{"definition":"abbreviation for Associate in Artsa degree given by an American college to someone after they have finished a two-year course, or a person who has this degree","examples":[]},{"definition":"abbreviation for Alcoholics Anonymousan organization for people who drink too much alcohol and want to cure themselves of this habit","examples":["an AA meeting"]},{"definition":"abbreviation for the Automobile Associationan organization in the UK that gives help and information to drivers who are members of it","examples":[]}]}]}
{"_id":{"$oid":"60c06feea54d753b12266639"},"word":"abacuses，我想查出包含两个连续音素（元音与辅音的任意组合）的音标对应英文单词，譬如“æb”，请给出 Python 代码，可能要用到正则表达式。进一步，请单独指出，如果是三个音标，如“kəs”，正则表达式部分要如何修改，才能满足查询要求。
```


POE 回复：
这个问题可以用 Python 和正则表达式来解决。以下是一个示例代码:

```python
import json
import re

# 读取 JSON 文件
with open('input.json', 'r') as f:
    data = json.load(f)

# 定义正则表达式模式
pattern_2 = r'[a-z]{1}\[a-z]{1}'
pattern_3 = r'[a-z]{1}\[a-z]{1}\[a-z]{1}'

# 遍历 JSON 数据并提取单词
for item in data:
    word = item['word']
    pronunciations = item['pos_items'][0]['pronunciations']
    
    # 检查是否包含两个连续音素
    for pronunciation in pronunciations:
        ipa = pronunciation['pronunciation']
        matches_2 = re.findall(pattern_2, ipa)
        matches_3 = re.findall(pattern_3, ipa)
        
        if matches_2:
            print(f"Word with two consecutive phonemes: {word}, IPA: {ipa}")
        elif matches_3:
            print(f"Word with three consecutive phonemes: {word}, IPA: {ipa}")
```

这个代码做了以下事情:

1. 读取 JSON 文件并将数据加载到 `data` 变量中。
2. 定义两个正则表达式模式:
   - `pattern_2`: 匹配两个连续的小写英文字母
   - `pattern_3`: 匹配三个连续的小写英文字母
3. 遍历 `data` 中的每个项目,并提取单词和发音信息。
4. 对于每个发音,使用 `re.findall()` 函数来检查是否包含两个或三个连续的音素。
5. 如果找到匹配,则输出相关信息。

如果要查找三个连续的音素(如 "kəs"),只需要修改 `pattern_3` 即可:

```python
pattern_3 = r'[a-z]{1}\[a-z]{1}\[a-z]{1}'
```

这个正则表达式模式会匹配三个连续的小写英文字母。

希望这个解决方案对你有帮助!如果还有任何问题,欢迎随时询问。



## 第二轮对话

第一轮的代码并不能很好满足需求，我下面的提问反馈出有些 ipa 字符不属于 a-z 26 个英文字母。

>我提问：
æ 也在正则表达式的[a-z]之间吗

> POE 答：
非常好的提问。你说得很对,正则表达式中的 `[a-z]` 只能匹配小写英文字母,而不能匹配 `æ` 等 IPA 符号。我们需要稍微修改一下正则表达式模式,以便能够匹配 IPA 字符。

修改后的代码如下:

```python
import json
import re

# 读取 JSON 文件
with open('input.json', 'r') as f:
    data = json.load(f)

# 定义正则表达式模式
pattern_2 = r'[a-z\u0250-\ue27f]{1}[a-z\u0250-\ue27f]{1}'
pattern_3 = r'[a-z\u0250-\ue27f]{1}[a-z\u0250-\ue27f]{1}[a-z\u0250-\ue27f]{1}'

# 遍历 JSON 数据并提取单词
for item in data:
    word = item['word']
    pronunciations = item['pos_items'][0]['pronunciations']
    
    # 检查是否包含两个或三个连续音素
    for pronunciation in pronunciations:
        ipa = pronunciation['pronunciation']
        matches_2 = re.findall(pattern_2, ipa)
        matches_3 = re.findall(pattern_3, ipa)
        
        if matches_2:
            print(f"Word with two consecutive phonemes: {word}, IPA: {ipa}")
        elif matches_3:
            print(f"Word with three consecutive phonemes: {word}, IPA: {ipa}")
```

主要变化是在正则表达式模式中添加了 `\u0250-\ue27f` 这个范围。这个范围覆盖了 IPA 字符集,所以现在可以匹配像 `æ` 这样的 IPA 字符了。使用这个更新后的代码,应该就可以正确地识别出包含两个或三个连续音素的单词了。



**我提问：IPA 字符集都有哪些**

> POE 答：
IPA（国际音标）字符集包含了大量的语音符号,用于精确描述各种语言的发音。主要包含以下几类字符:

1. 辅音符号:
   - 双辅音：如 [ts], [ʧ], [ʤ] 等
   - 单辅音：如 [p], [b], [t], [d], [k], [g] 等

2. 元音符号:
   - 元音：如 [i], [e], [æ], [a], [ɑ], [o], [u] 等
   - 圆唇元音：如 [y], [ø], [œ], [ɯ], [ɤ], [o] 等
   - 浊化元音：如 [ɛ̌], [ɔ̌], [ǎ] 等

3. 声调符号:
   - 平调：如 [˥], [˧], [˨] 等
   - 升调：如 [˩˧], [˨˦] 等
   - 降调：如 [˥˩], [˦˩] 等

4. 次强读符号：如 [ˈ], [ˌ]

5. 音节边界符号：如 [.], [#] 等

6. 连音符号：如 [ˌ], [‿] 等

7. 语音修饰符号：如 [̥], [̤], [̩], [˞] 等

这些符号可以组合使用,描述出各种复杂的语音细节。IPA 字符集广泛应用于语音学、语言学研究以及实际的发音标注中。如果你需要进一步了解,可以查阅 IPA 相关的参考资料。

------

下面才逐步接近我要找的答案：

## 第三轮对话

> 我继续提问：

```
我要查询任意几个（1 个-3 个）元音或者辅音组合（ipa 字符集的一部分），对应的音标以及符合条件的英文单词。请写一个查询函数，输入是上面的ipa 字符组合，函数功能部分，用正则表达式匹配 Json 文件中的内容，并输出满足要求的英文单词（Json 中关键词“word”）和音标（关键词“pronunciations”)，请写出 Python 代码。Json 文件格式如下：{"_id":{"$oid":"60c06f88a54d753a1e7ff079"},"word":"aardvarks","pos_items":[{"type":"noun","pronunciations":[{"region":"uk","audio":"https://dictionary.cambridge.org/media/english/uk_pron/u/uka/uka__/uka____009.mp3","pronunciation":"ˈɑːd.vɑːk"},{"region":"us","audio":"https://dictionary.cambridge.org/media/english/us_pron/u/usa/usad_/usad___007.mp3","pronunciation":"ˈɑːrd.vɑːrk"}],"definitions":[{"definition":"an African mammal with a long nose and large ears that lives underground and eats insects","examples":[]}]}]}
```



> POE 答复：

```
import json
import re

def query_ipa_words(ipa_pattern):
    # 读取 JSON 文件
    with open('input.json', 'r') as f:
        data = json.load(f)

    # 使用正则表达式匹配 IPA 模式
    matches = []
    for item in data:
        word = item['word']
        pronunciations = item['pos_items'][0]['pronunciations']
        for pronunciation in pronunciations:
            ipa = pronunciation['pronunciation']
            if re.search(ipa_pattern, ipa):
                matches.append((word, ipa))

    return matches
    
# 查询包含 [a], [ɑ], [o] 的单词
ipa_pattern = r'[aɑo]{1,3}'
results = query_ipa_words(ipa_pattern)
for word, ipa in results:
    print(f"Word: {word}, IPA: {ipa}")

# 查询包含 [p], [t], [k] 的单词
ipa_pattern = r'[ptk]{1,3}'
results = query_ipa_words(ipa_pattern)
for word, ipa in results:
    print(f"Word: {word}, IPA: {ipa}")
```



> 上述代码，经过我分析后，ipa_pattern 不是我想要的，我想要查询非 a-z 的字符，也就是 Ipa 字符。所以继续追问：
>
> 假如是æb，这两个单词，正则表达式如何匹配，注意æ是 ipa 字符。



> POE 答复，这回是我想要的答案：

好的,我明白了。对于 IPA 字符 æ,我们需要使用特殊的正则表达式来匹配。

下面是一个示例代码:

```python
import json
import re

def query_ipa_words(ipa_pattern):
    # 读取 JSON 文件
    with open('input.json', 'r') as f:
        data = json.load(f)

    # 使用正则表达式匹配 IPA 模式
    matches = []
    for item in data:
        word = item['word']
        pronunciations = item['pos_items'][0]['pronunciations']
        for pronunciation in pronunciations:
            ipa = pronunciation['pronunciation']
            if re.search(ipa_pattern, ipa):
                matches.append((word, ipa))

    return matches

# 查询包含 æ 和 b 的单词
ipa_pattern = r'æb'
results = query_ipa_words(ipa_pattern)
for word, ipa in results:
    print(f"Word: {word}, IPA: {ipa}")
```

在这个例子中,我们使用了 `r'æb'` 作为正则表达式模式。这里的 `æ` 是 IPA 字符,需要使用原始字符串的方式 `r'...'` 来表示,才能正确匹配。

这样,该函数就可以查找 JSON 文件中包含 `æb` 这个 IPA 字符组合的单词和对应的发音了。

如果你需要匹配更复杂的 IPA 字符组合,可以参考 IPA 字符集的正则表达式语法。例如,对于 `[a]`, `[ɑ]`, `[o]` 的组合,可以使用 `r'[aɑo]{1,3}'` 这样的正则表达式模式。

## 第三轮对话代码主体能用，就是要优化下

> Debug，因为 上面 JSON 文件是一次性读取，但是 JSON 文件过大（60 Mb），所以要逐行读取。
>
> ---------------------------------------------------------------------------
> JSONDecodeError                           Traceback (most recent call last)
> Cell In[3], line 25
>      23 # 查询包含 æ 和 b 的单词
>      24 ipa_pattern = r'æb'
> ---> 25 results = query_ipa_words(ipa_pattern)
>      26 for word, ipa in results:
>      27     print(f"Word: {word}, IPA: {ipa}")
>
> Cell In[3], line 9, in query_ipa_words(ipa_pattern)
>       6 def query_ipa_words(ipa_pattern):
>       7     # 读取 JSON 文件
>       8     with open('/Users/chengyong/Documents/01_Coding/Github-desktop-sync/macbook_computer_code/cam_dict.refined.json', 'r') as f:
> ----> 9         data = json.load(f)
>      11     # 使用正则表达式匹配 IPA 模式
>      12     matches = []
>
> File ~/anaconda3/envs/Jupyterlab_conda/lib/python3.8/json/__init__.py:293, in load(fp, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
>     274 def load(fp, *, cls=None, object_hook=None, parse_float=None,
>     275         parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
>     276     """Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
>     277     a JSON document) to a Python object.
>     278 
>    (...)
>     291     kwarg; otherwise ``JSONDecoder`` is used.
>     292     """
> --> 293     return loads(fp.read(),
>     294         cls=cls, object_hook=object_hook,
>     295         parse_float=parse_float, parse_int=parse_int,
>     296         parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
>
> File ~/anaconda3/envs/Jupyterlab_conda/lib/python3.8/json/__init__.py:357, in loads(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
>     352     del kw['encoding']
>     354 if (cls is None and object_hook is None and
>     355         parse_int is None and parse_float is None and
>     356         parse_constant is None and object_pairs_hook is None and not kw):
> --> 357     return _default_decoder.decode(s)
>     358 if cls is None:
>     359     cls = JSONDecoder
>
> File ~/anaconda3/envs/Jupyterlab_conda/lib/python3.8/json/decoder.py:340, in JSONDecoder.decode(self, s, _w)
>     338 end = _w(s, end).end()
>     339 if end != len(s):
> --> 340     raise JSONDecodeError("Extra data", s, end)
>     341 return obj
>
> JSONDecodeError: Extra data: line 2 column 1 (char 523)。报错如上，可能要一行一行读取 json



> POE 答复：

很抱歉,出现了这个错误。根据错误信息,这可能是因为 JSON 文件中包含了一些额外的数据导致的。

让我们尝试一行一行读取 JSON 文件,看看是否可以解决这个问题:

```python
import json
import re

def query_ipa_words(ipa_pattern):
    matches = []
    with open('/Users/chengyong/Documents/01_Coding/Github-desktop-sync/macbook_computer_code/cam_dict.refined.json', 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                word = data['word']
                pronunciations = data['pos_items'][0]['pronunciations']
                for pronunciation in pronunciations:
                    ipa = pronunciation['pronunciation']
                    if re.search(ipa_pattern, ipa):
                        matches.append((word, ipa))
            except (KeyError, IndexError):
                # 跳过无效或缺失数据的行
                continue

    return matches

# 查询包含 æ 和 b 的单词
ipa_pattern = r'æb'
results = query_ipa_words(ipa_pattern)
for word, ipa in results:
    print(f"Word: {word}, IPA: {ipa}")
```

在这个修改后的代码中,我们使用 `for line in f:` 来逐行读取 JSON 文件,并使用 `json.loads(line)` 来解析每一行。这样可以避免一次性读取整个 JSON 文件而出现的错误。

此外,我们还添加了一些异常处理,以便在遇到缺失或无效数据时跳过该行,继续处理下一行。

希望这个修改可以帮助你解决这个问题。如果还有任何其他问题,请随时告诉我。



## 继续优化，只匹配美式发音音标

> 我测试了下，是可以返回所有满足的单词的。但是同样符合`æb`特征的单词出现了两次。继续修改：
>
> 进一步，在上面 json 文件中，同一个单词，既有‘region’为"uk"的pronounciation，也有“us”的pronounciation，我只想去"us"的pronounciation中去匹配对应特定字符串，请修正代码。



> 这下才是最终我要得到的程序，以下是 POE 的答复：

我明白你的需求,这里是修改后的代码:

```python
import json
import re

def query_ipa_words(ipa_pattern):
    matches = []
    with open('/Users/chengyong/Documents/01_Coding/Github-desktop-sync/macbook_computer_code/cam_dict.refined.json', 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                word = data['word']
                pronunciations = [p for p in data['pos_items'][0]['pronunciations'] if p['region'] == 'us']
                for pronunciation in pronunciations:
                    ipa = pronunciation['pronunciation']
                    if re.search(ipa_pattern, ipa):
                        matches.append((word, ipa))
            except (KeyError, IndexError):
                # 跳过无效或缺失数据的行
                continue

    return matches

# 查询包含 æ 和 b 的单词
ipa_pattern = r'æb'
results = query_ipa_words(ipa_pattern)
for word, ipa in results:
    print(f"Word: {word}, IPA: {ipa}")
```

主要的修改如下:

1. 在 `pronunciations` 的赋值中,我们使用列表推导式 `[p for p in data['pos_items'][0]['pronunciations'] if p['region'] == 'us']` 来筛选出只包含 "us" region 的发音信息。
2. 这样就可以确保只处理美式发音,而忽略其他地区的发音信息。

现在,该代码应该可以满足你的需求了。如果还有其他问题,欢迎继续询问。