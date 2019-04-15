# jocipher
Cryptography

## Challenge 


Decrypt PIY{zsxh-sqrvufwh-nfgl} to get the flag!

made by Samantha Comeau

## Solution

	$ pip3 install --user uncompyle6

	$ uncompyle6 jocipher.pyc > jocipher_decompiled.py

	$ (for i in {1..100}; do python jocipher_decompiled.py --string 'PIY{zsxh-sqrvufwh-nfgl}' --decode --shift $i; done) | grep "WPI"
	WPI{mdzj-deycogrj-bgha}
	WPI{vsbh-seymofrh-xfgl}
	WPI{zaxg-aeyvodrg-ndfk}
	WPI{blnf-leyzosrf-csdj}
	WPI{xkcd-keyboard-mash}
	WPI{njms-jeyxolrs-vlag}
	WPI{chva-heynokra-zklf}
	WPI{mgzl-geycojrl-bjkd}
	WPI{vfbk-feymohrk-xhjs}
	WPI{zdxj-deyvogrj-ngha}

## Flag

	WPI{xkcd-keyboard-mash}
