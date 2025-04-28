# Vanilla to Paper world converter


# English

**VanillaToPaperWorldConverter** is a simple Python utility for converting a Minecraft Vanilla world into a structure compatible with **PaperMC** servers (`world`, `world_nether`, and `world_the_end`).

## Features

- Automatically copies the main world data.
- Correctly splits dimension data:
  - **Overworld** → `world`
  - **Nether (DIM-1)** → `world_nether`
  - **The End (DIM1)** → `world_the_end`
- Simple and user-friendly console interface.

## Installation and Usage

1. Download or clone this repository:

```bash
git clone https://github.com/MrSandSS/Vanilla-to-Paper-world-converter
```

2. Install required libraries:

```bash
pip install tqdm
```

3. Place the content of the world folder to `Vanilla_world` folder.

4. Make sure the `converted` directory is **empty**.

5. Run the program:

```bash
python main.py
```

6. Follow the on-screen instructions.

## Project Structure

```bash
VanillaToPaperWorldConverter/
│
├── converted/                 # The converted worlds will be saved here
├── Vanilla_world/             # Place your Vanilla world here
├── main.py                    # The main executable script
```

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

You are free to:
- Share — copy and redistribute the material in any medium or format
- Under the following terms:
  - Attribution — You must give appropriate credit (Radmir Belonogov aka MrSandSS).
  - NonCommercial — You may not use the material for commercial purposes.
  - NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified material.

Full license text can be found in the LICENSE file.



# Русский

**VanillaToPaperWorldConverter** — это простая утилита на Python для конвертации мира Minecraft из обычного (Vanilla) формата в структуру, совместимую с серверами **PaperMC** (`world`, `world_nether` и `world_the_end`).

## Возможности

- Автоматическое копирование основных данных мира.
- Правильное разделение данных измерений:
  - **Обычный мир** → `world`
  - **Незер (DIM-1)** → `world_nether`
  - **Энд (DIM1)** → `world_the_end`
- Простой и понятный интерфейс в консоли.

## Установка и использование

1. Скачайте или клонируйте репозиторий:

```bash
git clone https://github.com/MrSandSS/Vanilla-to-Paper-world-converter
```

2. Установите необходимые библиотеки:

```bash
pip install tqdm
```

3. Поместите содержимое папки с миром в папку `Vanilla_world`.

4. Убедитесь, что папка `converted` **пуста**.

5. Запустите программу:

```bash
python main.py
```

6. Следуйте инструкциям в консоли.

## Структура проекта

```bash
VanillaToPaperWorldConverter/
│
├── converted/                 # Здесь будут сохраняться конвертированные миры
├── Vanilla_world/             # Сюда нужно положить ваш мир Vanilla
├── main.py                    # Главный исполняемый скрипт
```

## Лицензия

Этот проект лицензирован по лицензии [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Вы можете:
- Копировать и распространять материал в любом формате.

На следующих условиях:
- Attribution — необходимо указать авторство (Radmir Belonogov aka MrSandSS).
- NonCommercial — запрещено использовать материал в коммерческих целях.
- NoDerivatives — при переработке материала запрещено распространять модифицированные версии.

Полный текст лицензии содержится в файле LICENSE.
