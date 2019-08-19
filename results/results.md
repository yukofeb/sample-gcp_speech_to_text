# GCP Speech-to-Textを試した結果
## speechsample01
### 音源
[スピード文字起こしサービス｜うちッパ](http://www.uchippa.com/service/)  
> サンプル音源Ａ(音質普通)  

* 男性が一人で話している  
* 少しごにょごにょした語り口  

```
それから、１０ページの意思決定システムです。 ここは、校務運営会議という会議が本校の意思決定機関になりますけれども、組織運営規定に従いましてきちっとやっていますよということです。真ん中にアンダーラインを引いたところがありますけれども、目的達成に適した効率的な校務分掌の構築が課題と考えている。年度ごとに、事業計画に基づき常に目標達成に適した体制に見直すということで、先ほどと同様に、基本的にはタイムリーにいろんなことに対応していきましょうということを課題としても掲げております。
```

### 結果
* 精度悪い  
* なぜか最初の方しか読み取れていない  

```
$ GOOGLE_APPLICATION_CREDENTIALS='./***.json' python sample.py speechsample01.flac
Transcript: N システムと誘拐されましたどこに行けばもらえるお金
Confidence: 0.8540006279945374
```


## speechsample02
### 音源
[サンプル音声 \| HOYA音声合成ソフトウェア VoiceText](https://voicetext.jp/samplevoice/)  
> 電話自動応答  

* 女性（合成音声）が一人で話している  
* はっきりとした語り口  

```
お電話ありがとうございます。こちらは発着案内サービスです。
12月25日の運航状況についてお知らせいたします。
成田国際空港の天気概況は概ね良好です。平常どおりの運航を予定しています。
```

### 結果
* 完璧な精度（句読点が無いのは仕様）  
  * USだと句読点をつけられるらしいが、日本語は未対応  
  [句読点の挿入  \|  Cloud Speech\-to\-Text  \|  Google Cloud](https://cloud.google.com/speech-to-text/docs/automatic-punctuation?hl=ja)  
  > 注: Speech-to-Text で音声文字変換の結果に句読点を挿入できるのは、en-US 言語のみです。  

原文  
```
$ GOOGLE_APPLICATION_CREDENTIALS='./***.json' python sample.py speechsample02.flac
Transcript: お電話ありがとうございますこちらは発着案内サービスです12月25日の運行状況についてお知らせ致します成田国際空港の電気街今日は概ね良好です平常通りの運行を予定しています
Confidence: 0.9344446063041687
```

## speechsample03
### 音源
[サンプル・データ 日本語話し言葉コーパス（CSJ）](https://pj.ninjal.ac.jp/corpus_center/csj/sample.html)  
> 課題思考対話音声  

* 男性と女性の会話  
* 音声が重なっている箇所や間があったり、かなり難しそう（実際のコールセンター音声はこれよりもきちんとしていそう）  

原文  
https://pj.ninjal.ac.jp/corpus_center/csj/trans-f/task-smp.trn  

### 結果
* 想像通り全くダメ  
* GCPは日本語で話者識別ができないため二人の会話が一緒に認識されている  
* しかも途中で認識が切れている。。  

```
$ GOOGLE_APPLICATION_CREDENTIALS='./***.json' python sample.py speechsample03.flac
Transcript: かけます僕の方には写真が入ってる私の方はお名前時計一言っていうのが細いマサイ知らない人がいっぱいいるの名前じゃちょっと読み上げてくれないの料理を料理屋の料理人もの人が米メガネかけてないですかですがセルジオ越後
Confidence: 0.9336581826210022
```

## speechsample04
### 音源
[サンプル・データ 日本語話し言葉コーパス（CSJ）](https://pj.ninjal.ac.jp/corpus_center/csj/sample.html)  
> 学会講演  

* 男性が講演している  
* 実際の話し言葉だがだがそこそこ明瞭に話している  

原文  
https://pj.ninjal.ac.jp/corpus_center/csj/trans-f/aps-smp.trn  

### 結果
* ほぼ完璧。マイクに近いような音声なので、認識しやすかったのでは  
* よく聞くと、文章の間にある「えー」が削除されている。GCP側で不要と認識して排除してくれているっぽい  

原文  
```
$ GOOGLE_APPLICATION_CREDENTIALS='./***.json' python sample.py speechsample04.flac
Transcript: パラ言語情報ということなんですが簡単に最初に復習をしておきたいと思いますがあのこうやって話しておりますとそれはもちろんあの言語的情報を伝えるという事が一つの重要な目的なんでありますが同時にパラ言語情報そして非言語情報が伝わっていますがこの散文方は藤崎先生によるものでしてパラ言語情報というのは要はあの意図的に作業できるわしゃがちゃんとコントロールして出してるんだけども言語情報と違って連続的に変化するからカテゴライズすることがやや難しいそういった状況であります
Confidence: 0.9510669708251953
```
