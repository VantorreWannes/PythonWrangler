from AffirmError import AffirmIsFalse


def affirm_ne(item, item2, error_message="Affirm_ne returned False."):
    try:
        assert item != item2
    except AssertionError:
        AffirmIsFalse(error_message).raise_to_level(2)


def affirm_eq(item, item2, error_message="Affirm_eq returned False."):
    try:
        assert item == item2
    except AssertionError:
        AffirmIsFalse(error_message).raise_to_level(2)


def affirm(item, error_message="Affirm returned False."):
    try:
        assert item
    except AssertionError:
        AffirmIsFalse(error_message).raise_to_level(2)


if __name__ == "__main__":
    affirm(False)
