import pytest
from name_format import full_name

# --- BASIC FORMATTING -----------------------------------------------------


def test_simple_first_last():
    assert full_name("steve nolan") == "Steve Nolan"


def test_two_args():
    assert full_name("steve", "nolan") == "Steve Nolan"


def test_title_casing():
    assert full_name("  aLiCe  ", "  o'connor  ") == "Alice O'Connor"


# --- IRISH PREFIXES -------------------------------------------------------


def test_o_apostrophe_brian_curly():
    assert full_name("ó brian") == "O'Brian"


def test_o_apostrophe_brian_ascii():
    assert full_name("o brian") == "O'Brian"


def test_o_apostrophe_attached():
    assert full_name("óbrien") == "O'Brien"


# --- MULTI-PART NAMES -----------------------------------------------------


def test_drop_middle_name():
    # michael  patrick  o'sullivan → Michael O'Sullivan
    assert full_name("michael patrick o'sullivan") == "Michael O'Sullivan"


def test_hyphenated_first_name():
    assert full_name("mary-kate o'reilly") == "Mary-Kate O'Reilly"


def test_keep_single_name():
    assert full_name("prince") == "Prince"


# --- PUNCTUATION CLEANING --------------------------------------------------


def test_strips_commas_dots():
    assert full_name("  . sinead , smith ") == "Sinead Smith"


def test_multiple_punctuations():
    assert full_name("o’brian;") == "O'Brian"


# --- INITIALS --------------------------------------------------------------


def test_initials():
    assert full_name("a.", "o'reilly") == "A. O'Reilly"


# --- PARTICLES -------------------------------------------------------------


def test_particles_lowercased():
    assert full_name("seamus de valera") == "Seamus de Valera"


def test_particles_first_word_not_lowercased():
    assert full_name("de valera") == "De Valera"
