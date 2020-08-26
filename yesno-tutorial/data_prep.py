#! /usr/bin/env python

import os
import os.path
import sys

zeroes = []
ones = []
for fn in os.listdir('waves_yesno'):
    if fn.startswith('0'):
        zeroes.append(fn)   # => training set
    elif fn.startswith('1'):
        ones.append(fn)     # => test set

def text(filenames):
    results = []
    for filename in filenames:
        basename = filename.split('.')[0]
        transcript = basename.replace('1', 'YES').replace('0', 'NO').replace('_', " ")
        results.append("{} {}".format(basename.split('.')[0], transcript))

    return '\n'.join(sorted(results))


# train -> zeroes
# test  -> ones

with open('data/train_yesno/text', 'w') as train_text, open('data/test_yesno/text', 'w') as test_text:
    train_text.write(text(zeroes))
    test_text.write(text(ones))

# finish this method
def wav_scp(filenames):
    results = []
    for filename in filenames:
        file_id = filename.split(".")[0]
        file_path = "waves_yesno/" + filename
        results.append("{} {}".format(file_id, file_path))
    return '\n'.join(sorted(results))




with open('data/train_yesno/wav.scp', 'w') as train_text, open('data/test_yesno/wav.scp', 'w') as test_text:
    train_text.write(wav_scp(zeroes))
    test_text.write(wav_scp(ones))


# finish this method
def utt2spk(filenames):
    results = []
    for filename in filenames:
        file_id = filename.split(".")[0]
        speaker = "global"
        results.append("{} {}".format(file_id, speaker))
    return '\n'.join(sorted(results))




with open('data/train_yesno/utt2spk', 'w') as train_text, open('data/test_yesno/utt2spk', 'w') as test_text:
    train_text.write(utt2spk(zeroes))
    test_text.write(utt2spk(ones))


# finish this method
# note that, spk2utt can be generated by using Kaldi util, once you have utt2spk file.
def spk2utt():
    results = []
    for filename in filenames:
        file_id = filename.split(".")[0]
        speaker = "global"
        results.append("{} {}".format(speaker, file_id))
    return '\n'.join(sorted(results))