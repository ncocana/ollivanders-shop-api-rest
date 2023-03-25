import pytest
from logic.GildedRose import (
    GildedRose,
    Item,
    NormalItem,
    ConjuredItem,
    AgedBrie,
    Sulfuras,
    Backstage,
)


# Define items to be tested.
@pytest.fixture
def items():
    normal_item = NormalItem("Normal Item", 10, 20)
    conjured_item = ConjuredItem("Conjured Item", 5, 30)
    aged_brie = AgedBrie("Aged Brie", 2, 0)
    sulfuras = Sulfuras("Sulfuras", 0, 80)
    backstage = Backstage("Backstage Passes", 15, 20)
    backstage_ten_days = Backstage("Backstage Passes", 10, 20)
    backstage_five_days = Backstage("Backstage Passes", 5, 20)

    return [
        normal_item,
        conjured_item,
        aged_brie,
        sulfuras,
        backstage,
        backstage_ten_days,
        backstage_five_days,
    ]


# Test for NormalItem class.
@pytest.mark.test_update_quality
def test_normal_item(items):
    normal_item = items[0]
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == 9
    assert normal_item.quality == 19


# Test for ConjuredItem class.
# Quality degrades twice as fast as normal items.
@pytest.mark.test_update_quality
def test_conjured_item(items):
    conjured_item = items[1]
    gilded_rose = GildedRose([conjured_item])
    gilded_rose.update_quality()
    assert conjured_item.sell_in == 4
    assert conjured_item.quality == 28


# Test for AgedBrie class.
# Increase in quality the older it gets.
@pytest.mark.test_update_quality
def test_aged_brie(items):
    aged_brie = items[2]
    gilded_rose = GildedRose([aged_brie])
    gilded_rose.update_quality()
    assert aged_brie.sell_in == 1
    assert aged_brie.quality == 1


# Test for Sulfuras class.
# Sell_in and quality do not change.
@pytest.mark.test_update_quality
def test_sulfuras(items):
    sulfuras = items[3]
    gilded_rose = GildedRose([sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.sell_in == 0
    assert sulfuras.quality == 80


# Test for Backstage class.
# Quality increases by 1 when there are more than 10 days.
@pytest.mark.test_update_quality
def test_backstage_normal(items):
    backstage = items[4]
    gilded_rose = GildedRose([backstage])
    gilded_rose.update_quality()
    assert backstage.sell_in == 14
    assert backstage.quality == 21


# Test for Backstage class.
# Quality increases by 2 when there are 10 days or less.
@pytest.mark.test_update_quality
def test_backstage_ten_days_or_less(items):
    backstage = items[5]
    gilded_rose = GildedRose([backstage])
    gilded_rose.update_quality()
    assert backstage.sell_in == 9
    assert backstage.quality == 22


# Test for Backstage class.
# Quality increases by 3 when there are 5 days or less.
@pytest.mark.test_update_quality
def test_backstage_five_days_or_less(items):
    backstage = items[6]
    gilded_rose = GildedRose([backstage])
    gilded_rose.update_quality()
    assert backstage.sell_in == 4
    assert backstage.quality == 23
