#!/usr/bin/env python3

import pytest

from armor_interaction import PredefinedArmorDb, DamageCalculator, ArmorLayer


@pytest.fixture
def armor_db() -> PredefinedArmorDb:
    db = PredefinedArmorDb()
    db.load_json()
    return db


@pytest.fixture
def damage_calculator() -> DamageCalculator:
    return DamageCalculator()


def test_get_armor_layers(armor_db: PredefinedArmorDb):
    assert (
        armor_db.get_armor_layers(
            [
                "Helmar's Shield of Meginbald",
                "Helmar's Warrior Priest Armour",
                "Helmar's Warrior Priest Armour (Padded Cap)",
            ],
            body_part="left_arm",
        )
        == [ArmorLayer("H", 2), ArmorLayer("M", 1), ArmorLayer("Ls", 2)]
    )
    
    
def test_get_damage(damage_calculator: DamageCalculator):
    assert (
        damage_calculator.get_damage(
            15,
            "p",
            8,
            [ArmorLayer("H", 2), ArmorLayer("M", 1), ArmorLayer("Ls", 2)],
        )[0]
        == 11
    )
