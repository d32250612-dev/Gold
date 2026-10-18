# TODO: реализовать функции по очереди и коммитить после каждой


def create_hero(name: str, hp: int, damage: int) -> dict:
    """Создаёт персонажа-героя и возвращает его как словарь."""
    hero ={
        "name":name,
        "hp":hp,
        'damage':damage,

    }
    return hero

      



def attack(attacker: dict, defender: dict) -> dict:
    """Атакующий наносит урон защитнику. Возвращает обновлённого защитника."""
    pass  # <- твой код здесь


def is_alive(hero: dict) -> bool:
    """Проверяет, жив ли герой (hp > 0)."""
    pass  # <- твой код здесь


def battle(hero: dict, monster: dict) -> str:
    """
    Простый бой: герой и монстр бьют друг друга по очереди,
    пока кто-то не умрёт. Возвращает строку 'hero' или 'monster'.
    """
    pass  # <- твой код здесь


# === ТЕСТЫ (раскомментируй, когда будешь проверять) ===
hero = create_hero("Артур", 100, 20)
print(hero)
# monster = create_hero("Гоблин", 50, 10)
# print(hero)
# monster = attack(hero, monster)
# print(monster)
# print(is_alive(monster))
# print(battle(hero, monster))

