# Copyright (c) 2020-2025, NVIDIA CORPORATION.
import os

import numpy as np
import pytest

import cudf
from cudf.core.wordpiece_tokenize import WordPieceVocabulary
from cudf.testing import assert_eq


@pytest.fixture(scope="module")
def datadir(datadir):
    return os.path.join(datadir, "")


@pytest.mark.parametrize("max_words", [0, 200, 10])
def test_text_wordpiece_tokenize(max_words, datadir):
    s = cudf.Series(
        [
            "The British Isles have been ringing for the last few years with the word  ' Art '  in its German sense ; ",
            "with  ' High Art ,  '   ' Symbolic Art ,  '   ' Ecclesiastical Art ,  '   ' Dramatic Art ,  '   ' Tragic Art ,  '  and so forth ; ",
            "and every well - educated person is expected ,  nowadays ,  to know something about Art . "
            "Yet in spite of all translations of German  ' AEsthetic '  treatises ,  and  ' Kunstnovellen ,  '  the mass of the British people cares very little about the matter ,  and sits contented under the imputation of  ' bad taste . ",
            " ' Our stage ,  long since dead ,  does not revive ;  our poetry is dying ;  our music ,  like our architecture ,  only reproduces the past ; ",
            "our painting is only first - rate when it handles landscapes and animals ,  and seems likely so to remain ; ",
            "but ,  meanwhile ,  nobody cares .   Some of the deepest and most earnest minds vote the question ,  in general ,  a  ' sham and a snare ,  '  and whisper to each other",
        ]
    )
    vocab_file = os.path.join(datadir, "vocab.txt")
    vc = cudf.read_text(vocab_file, delimiter="\n", strip_delimiters=True)
    wpt = WordPieceVocabulary(vc)
    wpr = wpt.tokenize(s, max_words)
    expected = cudf.Series(
        [
            cudf.Series(
                [
                    1109,
                    1418,
                    2181,
                    2897,
                    1138,
                    1151,
                    3170,
                    1158,
                    1111,
                    1103,
                    1314,
                    1374,
                    1201,
                    1114,
                    1103,
                    1937,
                    112,
                    2051,
                    112,
                    1107,
                    1157,
                    1528,
                    2305,
                    132,
                ],
                dtype=np.int32,
            ),
            cudf.Series(
                [
                    1114,
                    112,
                    1693,
                    2051,
                    117,
                    112,
                    112,
                    156,
                    1183,
                    1306,
                    1830,
                    1186,
                    2646,
                    1665,
                    2051,
                    117,
                    112,
                    112,
                    142,
                    1665,
                    1665,
                    2897,
                    1465,
                    2050,
                    1596,
                    1348,
                    2051,
                    117,
                    112,
                    112,
                    1987,
                    2312,
                    2980,
                    1596,
                    2051,
                    117,
                    112,
                    112,
                    157,
                    1611,
                    1403,
                    1596,
                    2051,
                    117,
                    112,
                    1105,
                    1177,
                    1111,
                    1582,
                    132,
                ],
                dtype=np.int32,
            ),
            cudf.Series(
                [
                    1105,
                    1451,
                    1218,
                    118,
                    174,
                    1181,
                    1358,
                    2599,
                    1906,
                    1825,
                    1110,
                    2637,
                    117,
                    1208,
                    1161,
                    1810,
                    1183,
                    1116,
                    117,
                    1106,
                    1221,
                    1380,
                    1164,
                    2051,
                    119,
                    162,
                    2105,
                    1107,
                    188,
                    1643,
                    3150,
                    1104,
                    1155,
                    189,
                    1611,
                    2316,
                    1742,
                    2116,
                    1116,
                    1104,
                    1528,
                    112,
                    138,
                    2036,
                    2050,
                    1324,
                    2105,
                    1596,
                    112,
                    189,
                    1874,
                    2980,
                    1548,
                    1279,
                    117,
                    1105,
                    112,
                    148,
                    3488,
                    2050,
                    2728,
                    2707,
                    2339,
                    1424,
                    117,
                    112,
                    1103,
                    3367,
                    1104,
                    1103,
                    1418,
                    1234,
                    1920,
                    1116,
                    1304,
                    1376,
                    1164,
                    1103,
                    2187,
                    117,
                    1105,
                    3465,
                    1116,
                    3438,
                    1174,
                    1223,
                    1103,
                    178,
                    1306,
                    1643,
                    1358,
                    1777,
                    2116,
                    1104,
                    112,
                    2213,
                    189,
                    2225,
                    1566,
                    119,
                ],
                dtype=np.int32,
            ),
            cudf.Series(
                [
                    112,
                    3458,
                    2016,
                    117,
                    1263,
                    1290,
                    2044,
                    117,
                    1674,
                    1136,
                    1231,
                    1964,
                    2109,
                    132,
                    1412,
                    185,
                    1186,
                    2105,
                    1616,
                    1110,
                    173,
                    1183,
                    1158,
                    132,
                    1412,
                    1390,
                    117,
                    1176,
                    1412,
                    170,
                    1197,
                    1732,
                    3150,
                    1665,
                    1204,
                    3313,
                    117,
                    1178,
                    1231,
                    1643,
                    2180,
                    1181,
                    1358,
                    2093,
                    1116,
                    1103,
                    1763,
                    132,
                ],
                dtype=np.int32,
            ),
            cudf.Series(
                [
                    1412,
                    2489,
                    1916,
                    1110,
                    1178,
                    1148,
                    118,
                    2603,
                    1165,
                    1122,
                    1289,
                    2897,
                    1657,
                    1116,
                    2599,
                    3186,
                    1116,
                    1105,
                    1126,
                    1182,
                    1918,
                    3447,
                    117,
                    1105,
                    3093,
                    2620,
                    1177,
                    1106,
                    3118,
                    132,
                ],
                dtype=np.int32,
            ),
            cudf.Series(
                [
                    1133,
                    117,
                    1928,
                    2246,
                    3031,
                    1513,
                    117,
                    1185,
                    1830,
                    1186,
                    1181,
                    1183,
                    1920,
                    1116,
                    119,
                    1789,
                    1104,
                    1103,
                    1996,
                    2556,
                    1105,
                    1211,
                    174,
                    1813,
                    1673,
                    2050,
                    1713,
                    1116,
                    2992,
                    1103,
                    2304,
                    117,
                    1107,
                    1704,
                    117,
                    170,
                    112,
                    188,
                    2522,
                    1105,
                    170,
                    188,
                    1605,
                    1874,
                    117,
                    112,
                    1105,
                    192,
                    3031,
                    1116,
                    3365,
                    1106,
                    1296,
                    1168,
                ],
                dtype=np.int32,
            ),
        ]
    )
    if max_words == 10:
        expected = cudf.Series(
            [
                cudf.Series(
                    [
                        1109,
                        1418,
                        2181,
                        2897,
                        1138,
                        1151,
                        3170,
                        1158,
                        1111,
                        1103,
                        1314,
                        1374,
                    ],
                    dtype=np.int32,
                ),
                cudf.Series(
                    [
                        1114,
                        112,
                        1693,
                        2051,
                        117,
                        112,
                        112,
                        156,
                        1183,
                        1306,
                        1830,
                        1186,
                        2646,
                        1665,
                        2051,
                        117,
                    ],
                    dtype=np.int32,
                ),
                cudf.Series(
                    [
                        1105,
                        1451,
                        1218,
                        118,
                        174,
                        1181,
                        1358,
                        2599,
                        1906,
                        1825,
                        1110,
                        2637,
                        117,
                        1208,
                        1161,
                        1810,
                        1183,
                        1116,
                    ],
                    dtype=np.int32,
                ),
                cudf.Series(
                    [112, 3458, 2016, 117, 1263, 1290, 2044, 117, 1674, 1136],
                    dtype=np.int32,
                ),
                cudf.Series(
                    [
                        1412,
                        2489,
                        1916,
                        1110,
                        1178,
                        1148,
                        118,
                        2603,
                        1165,
                        1122,
                        1289,
                        2897,
                    ],
                    dtype=np.int32,
                ),
                cudf.Series(
                    [
                        1133,
                        117,
                        1928,
                        2246,
                        3031,
                        1513,
                        117,
                        1185,
                        1830,
                        1186,
                        1181,
                        1183,
                        1920,
                        1116,
                        119,
                        1789,
                        1104,
                        1103,
                    ],
                    dtype=np.int32,
                ),
            ]
        )
    assert_eq(expected, wpr)
