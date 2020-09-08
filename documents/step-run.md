# step1

prepare_data.sh

After applying s1.sh, we can get a new folder named "data" which contains three subfolders (exclude .orig folder) "dev", "test" and "train".
Seven files are generated:

- reco2file_and_channel: Only required when audios were recorded in dual channels (e.g. for telephony conversational setup - one speaker on each side).

- segements: Contains mappings between utterance segmentation/alignment information and recording files.

- spk2utt: Simply inverse-indexed utt2spk (<speaker_id> <all_hier_utterences>)

- text: Essentially, transcripts of the audio files.

- utt2spk: For each utterance, mark which speaker spoke it.<utt_id> <speaker_id>

- wav.scp: <file_id> <path of wave filenames OR command to get wave file>

- stm & glm:If your data consists of a test set from NIST that has an "stm" and a "glm" file provided so that you can measure WER, then you can put these files in the data directory with the names "stm" and "glm". Note that we put the scoring script (which measures WER) in local/score.sh, which means it is specific to the setup; not all of the scoring scripts in all of the setups will recognize the stm and glm file. An example of a scoring script that uses those files is the one the Switchboard setup, i.e. egs/swbd/s5/local/score_sclite.sh, which is invoked by the top-level scoring script egs/swbd/s5/local/score.sh if it notices that your test set has the stm and glm files. (from kaldi-asr.org)

some contents comes from [this tutorial](https://github.com/keighrim/kaldi-yesno-tutorial)

# step 2

prepare_dict.sh

In data/local/dict_nosp, five files are generated:

- lexicon.txt: full list of lexeme-phone pairs including silences

- lexicon_words.txt: list of word-phone pairs (no silence)

- silence_phones.txt: list of silent phones.

- nonsilence_phones.txt: list of non-silent phones

- optional_silence.txt: list of optional silent phones (here, this looks the same as silence_phones.txt)

note: silence (SIL), spoken noise (SPN), non-spoken noise (NSN), and laughter (LAU).

# step 3

utils/prepare_lang.sh <dict-src-dir> <oov-dict-entry> <tmp-dir> <lang-dir>

The label <UNK> which is the dictionary word we will map OOV words to when appear in transcripts (this becomes data/lang/oov.txt). OOV: out of vocabulary.

path data/lang_nosp is created.


# step 4

local/ted_train_lm.sh

Start to train language model
format_arpa_lm.py: succeeded formatting ARPA lm from data/local/local_lm/data/lm_4_prune_small

# step 5
Run local/format_lms.sh

# step 6 
Get feature MFCC and in data/dev/data path, mfcc is saved here.
Explanation of scp and ark.

scp 文件是ark文件的索引，第一列的是utterance id，而通过id，就可以找到对应的ark文件。
根据[介绍](http://fancyerii.github.io/kaldidoc/tutorial2/)，可以通过copy-feats命令，将它ark转化为文本文件查看。
如果想要找到第十个录音特征，可以使用：
head -10 xxxxxxx.scp | tail -1 | copy-feats scp:- ark,t:- | head
拆解成，head -10 找到前十行，并使用tail -1获得其中的最后一行，将它作为copy-feats的输入，这样就会读取对应的特征了。

说明如何读取的字符串叫做rspecifier，例如：ark:gunzip -c my/dir/foo.ark.gz|

说明怎么写文件的字符串叫做wspecifier，比如”ark,t:foo.ark” 它的意思是输出为ark文件，并且是文本格式的，到foo.ark文件

# step 7
From comment of run.sh:
Now we have 452 hours of training data. Well create a subset with 10k short segments to make flat-start training easier.

# Step 8

