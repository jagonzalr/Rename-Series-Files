
# coding:utf-8

"""
MIT License

Copyright (c) 2016 José Antonio González Rodríguez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


from os import listdir, name, rename
from os.path import isfile, isdir, join, splitext
from sys import argv, exit


def getFiles(path):
    return [join(path, f) for f in listdir(path)
            if isfile(join(path, f)) and f[:1] is not '.']


def renameFiles(path, files, name, sequence, has_subtitles):
    for file in files:
        sequence_str = "0%d" % sequence if sequence < 10 else str(sequence)
        _, ext = splitext(file)
        if has_subtitles == "yes":
            if ext == '.srt':
                sequence += 1
        else:
            sequence += 1

        rename(file, path + "/" + name + sequence_str + ext)
        printArgs = (file, path, name, sequence_str, ext)
        print "RENAMING FILE %s TO %s/%s%s%s" % printArgs


def verifyArgs():
    if len(argv) != 5:
        print "Usage: python %s [diretory path] [new name] \
            [start sequence (number)] [has subtitiles (yes or no)]" % argv[0]

        exit(0)
    else:
        return argv


def verifyPath(path):

    if not isdir(path):
        print "The provided path '%s' is not a directory or does not \
            exists." % path

        exit(0)


if __name__ == '__main__':
    script, path, name, sequence, has_subtitles = verifyArgs()
    sequence = int(sequence)
    has_subtitles = str(has_subtitles).lower()
    print "<===== RUNNING SCRIPT: %s =====>" % script
    verifyPath(path)
    renameFiles(path, getFiles(path), name, sequence, has_subtitles)
    print "<===== END SCRIPT: %s =====>" % script
