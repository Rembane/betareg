# README

These are instructions will be partial and fragmentary at best. If there is something unclear about them, please open an issue.

## Prerequesites

You need a STM32F4 discovery board. They are discontinued which makes this endeavour a bit more interesting.

## Installation instructions

Make a virtualenv and then run `pip install -r requirements.txt` to install `rshell` and other nice tools.

Follow the guide on the [Micropython homepage](https://github.com/micropython/micropython/wiki/Board-STM32F407-Discovery)

`rshell` is an amazing replacement for Minicom, use it instead, it will find your board just fine.

But instead of running the make-command. Download the newest STM32F4 Discovery board dfu-file from [the Micropython download page](http://micropython.org/download).

[This is another guide](http://www.kaltpost.de/?p=2082), it should also work but needs other gear and that you have compiled the micropython parts yourself.

### Hints

Look for BOOT0 at the left side of the board, when the pin labels are turned correctly and the sound jack is at the bottom of the card.

## References

- [The STM32F4 Discovery board reference manual](http://www.st.com/content/ccc/resource/technical/document/user_manual/70/fe/4a/3f/e7/e1/4f/7d/DM00039084.pdf/files/DM00039084.pdf/jcr:content/translations/en.DM00039084.pdf)
