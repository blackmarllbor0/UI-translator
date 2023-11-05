# Translator

A translator that can be run both in your terminal and in a web browser, or even not run at all and the program itself will read your text from save buffer and insert a translation into it.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Run commands](#run-commands)
- [Contact Us](#contact-us)

## Introduction

If you want to translate quickly, you can just run `trans` and then the text you have saved on the clipboard will be read and replaced with the translation, buf if you want to enter new text, you can just run `trans -i="your any text"`.

You can also run the **UI** in a terminal or web browser.

For a more detailed on the startup commands, refer to block [Run Commands](#Run)

## Getting Started

1. To use the application, you first need to clone this get repository to your machine.

```bash
git clone https://github.com/blackmarllbor0/UI-translator.git
```

2. After that, you need to perform installation og the application.

```bash
pip install .
```

3. Great, now you can use the app! Use `trans` command.

## Configuration

The configuration file looks like this:

```yaml
storage:
  lang:
    src: "auto"
    dest: "en"
  translate_api: "google"
  open_in: "none"
  buffer:
    paste: true
    copy: true
  print: true
```

1. **lang** - Responsible for controlling the default language
   1. **src** - The default setting is **auto**, that's, it determines the language you enter. If you're sure that you will use only one language, you can change it with the command `trans -sc -src="new_lang"`.
   2. **dest** - The language into which the input text will be translated. The default setting is **en**. To change if you can use command `trans -sc -dest="new_lang"`.
2. **translate_api** - This is translator API. The default is [**google**](https://translate.google.com/), with plans to add [**yandex**](https://translate.yandex.ru/) and [**deepl**](https://www.deepl.com/translator) in the future. To change this field, you can use command `trans -sc -api="api"`
3. **open_in** - This item is responsible for where the application will open. The default setting is **none**, but you can also select **terminal** or **browser**. To change this field, you can use command `trans -sc -o="terminal"`.
4. **buffer** - This field is responsible for you clipboard.
   1. **paste** - If the value is `true`, the program, when opened, reads your buffer and translates the last copied text. To change this field, you can use command `trans -sc -paste=bool`.
   2. **copy** - If the value is `true`, the program saves the translation to your buffer when translating text. To change this field, you can use command `trans -sc -copy=bool`
5. **print** - Only works in `open_in: "none"` mode. The default setting is **true**. Outputs a string with the translation result. To change this field, you can use command `trans -sc -p=bool`

## Run commands

```bash
trans -[keys]
```

The application supports multiple startup methods, as well as many commands to control the startup of the application.

> If no configuration change key is specified, the keys passed will only work in the current session.

1. **Commands for configuration management**. The `-sc` or `--set-config` key must necessarily be present to change the configuration. To change configuration, you can add the keys below to these keys.
2. **Language control**
   1. `-src` - to change the source language.
   2. `-dest` - to change destination language.
3. **Translation API**. The `-api` key to change **API** for translation.
4. **Open app in** to open an application. Keys `-o` or `--open`.
5. **Buffer**
   1. `-paste` to change **paste** value.
   2. `-copy` to change **copy** value.
6. **Print result**. Use keys `-p` or `--print` to change **print** value.

## Contact Us

If you have any questions, suggestions, or encounter any issues, please feel free to reach out to us:

- Telegram: [@blackmarllbor0](https://t.me/blackmarllbor0)
- Email: 3100194@gmail.com

Thank you for your attention! I hope that my work will be useful to you!
