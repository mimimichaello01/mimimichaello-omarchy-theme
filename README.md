# Mimimichaello for Omarchy

Персональная тёмная тема для Omarchy, собранная на основе визуального стиля
Marvin. Репозиторий содержит как обычные файлы темы, так и дополнительный
установщик полного визуального слоя.

## Что входит в тему

- тёмная палитра и набор обоев;
- скругление и прозрачность окон;
- внутренние и внешние отступы по 8 px;
- тень и тонкая граница активного окна;
- анимации открытия и закрытия окон и `slide` между workspace;
- уведомления в стиле Marvin;
- Lock screen с надписью `mimimichaello`;
- Plymouth/SDDM unlock с надписью `mimimichaello`;
- GTK-тема Graphite-Dark;
- шрифты Inter и Libre Baskerville;
- отключённые автоматические screensaver и idle lock.

Тема не устанавливает оформление VS Code и не удаляет сторонние плагины или
текущую раскладку панели Omarchy.

## Установка

Рекомендуемое имя GitHub-репозитория — `mimimichaello`. Тогда Omarchy установит
его в путь, который используется в командах ниже.

```bash
omarchy theme install https://github.com/mimimichaello01/mimimichaello-omarchy-theme.git
```

Затем выберите один из двух вариантов.

### Вариант 1: визуальный слой без загрузочного экрана

```bash
~/.config/omarchy/themes/mimimichaello/install/mimimichaello
```

Команда применит тему, настройки Hyprland, уведомления, Lock screen, GTK и
шрифты. Системный Plymouth при этом не изменяется.

### Вариант 2: полная установка с Plymouth

```bash
~/.config/omarchy/themes/mimimichaello/install/mimimichaello --with-plymouth
```

Дополнительно будет применён экран ввода пароля при запуске компьютера.
Omarchy запросит `sudo`, потому что для Plymouth требуется обновление системных
файлов загрузки.

## Другие команды

Показать текущее состояние:

```bash
~/.config/omarchy/themes/mimimichaello/install/mimimichaello --status
```

Вернуть состояние, сохранённое перед первым запуском установщика:

```bash
~/.config/omarchy/themes/mimimichaello/install/mimimichaello --revert
```

Если тема устанавливалась с `--with-plymouth`, команда `--revert` также вернёт
предыдущий Plymouth и может запросить `sudo`.

## Как работает восстановление

Перед первым применением установщик сохраняет изменяемые пользовательские
файлы и настройки в:

```text
~/.local/state/mimimichaello/snapshot/
```

Повторный запуск обновляет визуальный слой, но не перезаписывает первоначальный
снимок. Благодаря этому `--revert` возвращает состояние, которое было до самой
первой установки.

## Обновление темы

После обновления файлов репозитория снова запустите нужный вариант установщика:

```bash
~/.config/omarchy/themes/mimimichaello/install/mimimichaello
```

или:

```bash
~/.config/omarchy/themes/mimimichaello/install/mimimichaello --with-plymouth
```

Установщик рассчитан на повторный запуск: он не добавляет дубликаты настроек и
сохраняет первоначальный снимок для отката.
