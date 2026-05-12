def test_policy_imports():
    from openfisca_policy import AbstractAggregates, SimulationBuilder
    from openfisca_policy.calmar import calmar
    from openfisca_policy.coicop import build_coicop_level_nomenclature
    from openfisca_policy.legislation_asof import parameters_asof
    from openfisca_policy.matching import nnd_hotdeck

    assert AbstractAggregates is not None
    assert SimulationBuilder is not None
    assert calmar is not None
    assert parameters_asof is not None
    assert nnd_hotdeck is not None
    assert build_coicop_level_nomenclature is not None
