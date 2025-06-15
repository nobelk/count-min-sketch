from src.count_min_sketch.cms import CMS
from src.count_min_sketch.cms import Item


class Flower(Item):
    def __init__(self, name: str):
        self._name = name

    def __repr__(self):
        return self._name


def test_cms_default():
    cms = CMS(100)
    data = ["daisy", "rose", "flora", "iris", "lily", "daisy", "rose", "flora", "iris", "lily", "daisy", "rose", "flora", "iris"]
    for item_name in data:
        flower = Flower(item_name)
        cms.update(flower)
    assert cms.query(Flower('rose')) == 3
    assert cms.query(Flower('lily')) == 2
    assert cms.query(Flower('Unknown flower')) == 0
