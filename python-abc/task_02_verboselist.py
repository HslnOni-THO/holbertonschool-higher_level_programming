#!/usr/bin/env python3
"""VerboseList that logs actions on list operations."""


class VerboseList(list):
    """A list that prints messages when items are added or removed."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        if len(self) == 0:
            print("Cannot pop from an empty list.")
            return None
        try:
            item = self[index]
            print(f"Popped [{item}] from the list.")
            return super().pop(index)
        except IndexError:
            print(f"Index [{index}] is out of range.")
            return None
