"""Twitterのデータが書かれたtxtファイルから、改行コードを除いてリストとして読み込んでいる"""
def processing(file):
    with open(file,encoding="utf-8_sig",errors='ignore') as f:
        data_raw = f.readlines()
        del data_raw[777126]
        del data_raw[0]
        data = []
        for i in range(len(data_raw)):
            c = re.sub("\n","",data_raw[i])
            data.append(c)
    return data

'''Twitterのデータに対して用いたLDAのコード（jupyterでやってて、関数として定義してなかったものを、ただくっつけたから間違いありそう）'''
def LDA('contents_all.txt'):
    with open("contents_all.txt",encoding="utf-8_sig",errors = "ignore") as f:
        data_sentences_test = f.readlines()
        #url,@消す
        data_sentences_3 = []
        for i in range(len(data_sentences_test[0:200])):
            a = re.sub("@([a-zA-Z0-9_]+)", "" ,data_sentences_test[i])
            b = re.sub("https([-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)","",a)
            c = re.sub("\n","",b)
            d = re.sub("#","",c)
            data_sentences_3.append(d)

        #同じ内容のツイート消す
        data_sentences_4 = list(set(data_sentences_3))
        #data_sentences_4 = data_sentences_3
        #data_sentences = data_sentences_2
        print(len(data_sentences_3))
        print(len(data_sentences_4))

        #形態素分析(trainデータに対して)
        mtt = MeCab.Tagger('-Ochasen')
        ori_test = []
        par_test = []
        for i in range(len(data_sentences_4)):
            node_test = mtt.parseToNode(data_sentences_4[i])
            origin_test = []
            parts_test = []
            while node_test:
                origin_test.append(node_test.surface)
                parts_test.append(node_test.feature.split(',')[0])
                node_test = node_test.next
            ori_test.append(origin_test) #[[品詞1,品詞2,...],[]]
            par_test.append(parts_test) #[[単語1,単語2,...],[単語1,単語2,...]]

        words_test = []
        word_count_test = []
        for j in range(len(par_test)):
            word_test = []
            for k in range(len(par_test[j])):
                if par_test[j][k] == "名詞":
                    word_test.append(ori_test[j][k])
                    word_count_test.append(ori_test[j][k])
                elif par_test[j][k] == "形容詞":
                    word_test.append(ori_test[j][k])
                    word_count_test.append(ori_test[j][k])
    #          elif par[j][k] == "動詞":
    #              word.append(ori[j][k])
    #              word_count.append(ori[j][k])
        word_ed_test = [e for e in word_test if e not in ng_word]
        words_test.append(word_ed_test)

        score_by_topic = defaultdict(int)
        test_corpus = [dictionary.doc2bow(text) for text in words_test]

        # クラスタリング結果を出力
        for unseen_doc, raw_train_text in zip(test_corpus, data_sentences_4):
            print(raw_train_text)
            for topic, score in lda[unseen_doc]:
                score_by_topic[int(topic)] = float(score)
            for i in range(num_topics):
                print('{:.2f}'.format(score_by_topic[i]), end='\t')
            print()
