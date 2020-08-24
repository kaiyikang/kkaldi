# Step 1 - Data preparation

dataset 60 .wav file 8kHz.
name: 1 ken/yes  0 lo/no

## Data preparation

split 60 wave files in half. 31 for traing, the rest for testing.

Create two return(py):
list of files in waves\_yesno.
two list, start with 0 and start with 1.

for each dataset, we need to generate kaldi input files representing our data.

- text
write an utterance per line, formatted in <utt\_id> <transcript>
<utt\_id> is filenames without extensions.
id needs to be a single token.(no whitespace inside allowed)

- wav.scp
indexing files to unique ids.
<file\_id> <path of wave filenames OR command to get wave file>
e.g.
~~~bash
0_1_0_0_1_0_1_1 waves_yesno/0_1_0_0_1_0_1_1.wav
~~~

file\_id is file name.

1 to 1 maping between utt_id and file_id

- utt2spk
For each utterance, mark which speaker spoke it.
Since yesno example has only one speaker, let's use global as speaker_id
<utt_id><speaker_id>
e.g.
0_0_1_0_1_0_1_1 global

- spk2utt

Simply inverse-indexed utt2spk

# Step 2 - Dictionary preparation

How to build language knowledge : lexicon and phone dictionaries.

## Lexicon
only two words yes/no

Assume they are one-phone.

Your dict directory should end up with these 5 dictionaries:

lexicon.txt: full list of lexeme-phone pairs including silences
lexicon_words.txt: list of word-phone pairs (no silence)
silence_phones.txt: list of silent phones
nonsilence_phones.txt: list of non-silent phones
optional_silence.txt: list of optional silent phones (here, this looks the same as silence_phones.txt)

