The treebanks directory include adapted versions of the original treebank, to match the UD2 guidelines. This pre-processing is done following the MaChAmp strategies: https://github.com/machamp-nlp/machamp/tree/master/scripts/udExtras

The used MaChAmp models can also be downloaded from: http://www.itu.dk/~robv/data/machamp/multi-lexnorm.tar.gz

To do the full extrinsic evaluation, it should be sufficient to copy over the submission folder to the extrEval directory, and then run each script in the scripts folder sequentially.


If you want to get results for a new normalization model:

* Provide normalization for the files in treebanks-cleaned/\*txt 
* Put the normalized files in the submissions folder
* Train MaChAmp (./scripts/1.machamp.train.sh) or download the models from the link above, and put them in machamp/logs/
* Run MaChAmp on the normalized file: 
```
python3 scripts/1.machamp.pred.py > 1.pred.sh
chmod +x 1.pred.sh
./1.pred.sh
```
* Now your submission should be included in the table: python3 scripts/2.extrTable.py

If you use this extrinsic evaluation, please cite the following sources:

```
TweeDe~\cite{rehbein-etal-2019-tweede}, AAE~\cite{blodgett-etal-2018-twitter}, MoNoise~\cite{van-der-goot-van-noord-2018-modeling}, Tweebank2~\cite{liu-etal-2018-parsing}. PoSTWITA~\cite{sanguinetti-etal-2018-postwita}, TWITTIRO~\cite{cignarella-etal-2019-presenting} and IWT151~\cite{pamay-etal-2015-annotation,sulubacak2018implementing}.


@inproceedings{rehbein-etal-2019-tweede,
    title = "twee{D}e {--} A {U}niversal {D}ependencies treebank for {G}erman tweets",
    author = "Rehbein, Ines  and
      Ruppenhofer, Josef  and
      Do, Bich-Ngoc",
    booktitle = "Proceedings of the 18th International Workshop on Treebanks and Linguistic Theories (TLT, SyntaxFest 2019)",
    month = aug,
    year = "2019",
    address = "Paris, France",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-7811",
    doi = "10.18653/v1/W19-7811",
    pages = "100--108"
}


@inproceedings{blodgett-etal-2018-twitter,
    title = "{T}witter {U}niversal {D}ependency Parsing for {A}frican-{A}merican and Mainstream {A}merican {E}nglish",
    author = "Blodgett, Su Lin  and
      Wei, Johnny  and
      O{'}Connor, Brendan",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P18-1131",
    doi = "10.18653/v1/P18-1131",
    pages = "1415--1425"
}


@inproceedings{van-der-goot-van-noord-2018-modeling,
    title = "Modeling Input Uncertainty in Neural Network Dependency Parsing",
    author = "van der Goot, Rob  and
      van Noord, Gertjan",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1542",
    doi = "10.18653/v1/D18-1542",
    pages = "4984--4991"
}


@inproceedings{liu-etal-2018-parsing,
    title = "Parsing Tweets into {U}niversal {D}ependencies",
    author = "Liu, Yijia  and
      Zhu, Yi  and
      Che, Wanxiang  and
      Qin, Bing  and
      Schneider, Nathan  and
      Smith, Noah A.",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N18-1088",
    doi = "10.18653/v1/N18-1088",
    pages = "965--975"
}

@inproceedings{sanguinetti-etal-2018-postwita,
    title = "{P}o{STWITA}-{UD}: an {I}talian {T}witter Treebank in {U}niversal {D}ependencies",
    author = "Sanguinetti, Manuela  and
      Bosco, Cristina  and
      Lavelli, Alberto  and
      Mazzei, Alessandro  and
      Antonelli, Oronzo  and
      Tamburini, Fabio",
    booktitle = "Proceedings of the Eleventh International Conference on Language Resources and Evaluation ({LREC} 2018)",
    month = may,
    year = "2018",
    address = "Miyazaki, Japan",
    publisher = "European Language Resources Association (ELRA)",
    url = "https://www.aclweb.org/anthology/L18-1279"
}

@inproceedings{cignarella-etal-2019-presenting,
    title = "Presenting {TWITTIR{\`O}}-{UD}: An {I}talian {T}witter Treebank in {U}niversal {D}ependencies",
    author = "Cignarella, Alessandra Teresa  and
      Bosco, Cristina  and
      Rosso, Paolo",
    booktitle = "Proceedings of the Fifth International Conference on Dependency Linguistics (Depling, SyntaxFest 2019)",
    month = aug,
    year = "2019",
    address = "Paris, France",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-7723",
    doi = "10.18653/v1/W19-7723",
    pages = "190--197"
}

@inproceedings{pamay-etal-2015-annotation,
    title = "The Annotation Process of the {ITU} Web Treebank",
    author = {Pamay, Tu{\u{g}}ba  and
      Sulubacak, Umut  and
      Toruno{\u{g}}lu-Selamet, Dilara  and
      Eryi{\u{g}}it, G{\"u}l{\c{s}}en},
    booktitle = "Proceedings of The 9th Linguistic Annotation Workshop",
    month = jun,
    year = "2015",
    address = "Denver, Colorado, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W15-1610",
    doi = "10.3115/v1/W15-1610",
    pages = "95--101"
}

@article{sulubacak2018implementing,
    title={Implementing universal dependency, morphology, and multiword expression annotation standards for Turkish language processing},
    author={Sulubacak, Umut and Eryi{\u{g}}it, G{\"u}l{\c{s}}en},
    journal={Turkish Journal of Electrical Engineering \& Computer Sciences},
    volume={26},
    number={3},
    pages={1662--1672},
    year={2018},
    publisher={The Scientific and Technological Research Council of Turkey}
}


```

