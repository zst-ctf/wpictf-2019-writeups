# fastoctothorp
Cryptography

## Challenge 

I need some help recovering my password. I managed to get a dump that contains its xxHash. It will be pretty hard to recover because of the strong password policy.

Exactly 6 lowercase letters
Seed is less then 10000
Flag is WPI{password+seed} (password+seed is the password valued with the seed concatenated. No +.)

made by acurless


## Solution


$ gem install --user-install ruby-xxHash

## Flag

	??