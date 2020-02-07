import pytest
from uk_postcode_validator.exceptions import PostcodeNotValidated


def test_uk_postcode_validator_constructor(raw_uk_postalcode, uk_postalcode_validator_instance):
    assert uk_postalcode_validator_instance.raw_postcode == raw_uk_postalcode


def test_uk_postcode_validator_string_conversion(raw_uk_postalcode, uk_postalcode_validator_instance):
    assert f"{uk_postalcode_validator_instance}" == raw_uk_postalcode


@pytest.mark.parametrize(
    "raw_postcode",
    (
        "EC1A 1BB",
        "W1A 0AX",
        "M1 1AE",
        "B33 8TH",
        "CR2 6XH",
        "DN55 1PT",
        "SW1W 0NY",
        "PO16 7GZ",
        "GU16 7HF",
        "L1 8JQ",
    ),
)
def test_uk_postcode_validator_validate_lowercase_postcodes(raw_postcode, uk_postalcode_validator):
    assert uk_postalcode_validator(raw_postcode.lower()).validate() is True


@pytest.mark.parametrize(
    "raw_postcode",
    (
        "EC1A 1BB",
        "W1A 0AX",
        "M1 1AE",
        "B33 8TH",
        "CR2 6XH",
        "DN55 1PT",
        "SW1W 0NY",
        "PO16 7GZ",
        "GU16 7HF",
        "L1 8JQ",
    ),
)
def test_uk_postcode_validator_validate_uppercase_postcodes(raw_postcode, uk_postalcode_validator):
    assert uk_postalcode_validator(raw_postcode).validate() is True


@pytest.mark.parametrize(
    "raw_postcode",
    (
        "VG1110",
        "VG1130",
        "CR 03",
        "GE 05",
        "SB 01",
        "KY1-11001",
        "KY2-2101",
        "MSR1120",
        "MSR1250",
        "AI-2640",
        "ASCN 1ZZ",
        "BBND 1ZZ",
        "BFPO 57",
        "BF1 2AT",
        "BFPO 58",
        "BF1 2AU",
        "BIQQ 1ZZ",
        "FIQQ 1ZZ",
        "GX11 1AA",
        "PCRN 1ZZ",
        "SIQQ 1ZZ",
        "STHL 1ZZ",
        "TDCU 1ZZ",
        "TKCA 1ZZ",
        "BS98 1TL",
        "BX1 1LT",
        "BX2 1LB",
        "BX3 2BB",
        "BX4 7SB",
        "BX5 5AT",
        "CF10 1BH",
        "CF99 1NA",
        "CV4 8UW",
        "CV35 0DB",
        "DA1 1RT",
        "DE99 3GG",
        "DE55 4SW",
        "DH98 1BT",
        "DH99 1NS",
        "E14 5HQ",
        "E14 5JP",
        "E16 1XL",
        "E20 2AQ",
        "E20 2BB",
        "E20 2ST",
        "E20 3BS",
        "E20 3EL",
        "E20 3ET",
        "E20 3HB",
        "E20 3HY",
        "E98 1SN",
        "E98 1ST",
        "E98 1TT",
        "EC2N 2DB",
        "EC4Y 0HQ",
        "EH12 1HQ",
        "EH99 1SP",
        "G58 1SB",
        "GIR 0AA",
        "IV21 2LR",
        "L30 4GB",
        "LS98 1FD",
        "M50 2BH",
        "M50 2QH",
        "N1 9GU",
        "N81 1ER",
        "NE1 4ST",
        "NG80 1EH",
        "NG80 1LH",
        "NG80 1RH",
        "NG80 1TH",
        "PH1 5RB",
        "PH1 2SJ",
        "S2 4SU",
        "S6 1SW",
        "S14 7UP",
        "SA99",
        "SE1 0NE",
        "SE1 8UJ",
        "SM6 0HB",
        "SN38 1NW",
        "SR5 1SU",
        "SW1A 0AA",
        "SW1A 0PW",
        "SW1A 1AA",
        "SW1A 2AA",
        "SW1A 2AB",
        "SW1H 0TL",
        "SW1P 3EU",
        "SW1W 0DT",
        "SW11 7US",
        "SW19 5AE",
        "TW8 9GS",
        "W1A 1AA",
        "W1D 4FA",
        "W1N 4DJ",
        "W1T 1FB",
        "CO4 3SQ",
    ),
)
def test_uk_postcode_validator_validate_special_cases(raw_postcode, uk_postalcode_validator):
    assert uk_postalcode_validator(raw_postcode).validate() is True


def test_uk_postcode_validator_outward_raises_exception_when_not_validated(uk_postalcode_validator):
    postcode_instance = uk_postalcode_validator("EC1A 1BB")
    with pytest.raises(PostcodeNotValidated):
        postcode_instance.outward


@pytest.mark.parametrize(
    "raw_postcode, expected_outward",
    (
        ("EC1A 1BB", "EC1A"),
        ("W1A 0AX", "W1A"),
        ("M1 1AE", "M1"),
        ("AI-2640", "AI"),
        ("KY1-1300", "KY1"),
        ("MSR1110", "MSR1110"),  # what's the outward in this cases?
    ),
)
def test_uk_postcode_validator_outward_result(raw_postcode, expected_outward, uk_postalcode_validator):
    postcode_instance = uk_postalcode_validator(raw_postcode)
    postcode_instance.validate()

    assert postcode_instance.outward == expected_outward
