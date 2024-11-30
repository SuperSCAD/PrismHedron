from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2
from super_scad_smooth_profiles.Chamfer import Chamfer
from super_scad_smooth_profiles.Fillet import Fillet

from super_scad_prism_hedron.SmoothPrismHedron import SmoothPrismHedron
from test.ScadTestCase import ScadTestCase


class SmoothPrismHedronTest(ScadTestCase):
    """
    Testcases for SmoothPrismHedron.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_prism(self):
        """
        Test a plain prism.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        nodes = [Vector2(0.0, 0.0),
                 Vector2(0.0, 60.0),
                 Vector2(60.0, 0.0)]

        prism = SmoothPrismHedron(height=50.0,
                                  points=nodes)

        self.assertFalse(prism.center)
        self.assertAlmostEqual(prism.height, 50.0)
        self.assertIsNone(prism.convexity)
        self.assertIsInstance(prism.extend_by_eps_sides, set)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(prism, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_prism_centered(self):
        """
        Test a centered prism.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        nodes = [Vector2(0.0, 0.0),
                 Vector2(0.0, 60.0),
                 Vector2(60.0, 0.0)]

        prism = SmoothPrismHedron(height=50.0,
                                  points=nodes,
                                  center=True)

        self.assertTrue(prism.center)
        self.assertAlmostEqual(prism.height, 50.0)
        self.assertIsNone(prism.convexity)
        self.assertIsInstance(prism.extend_by_eps_sides, set)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(prism, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_smooth_prism(self):
        """
        Test a smooth prism.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        nodes = [Vector2(0.0, 0.0),
                 Vector2(0.0, 60.0),
                 Vector2(60.0, 0.0)]

        prism = SmoothPrismHedron(height=50.0,
                                  points=nodes,
                                  profile_top=Fillet(radius=5.0),
                                  profile_verticals=Fillet(radius=5.0),
                                  profile_bottom=Chamfer(skew_length=5.0))

        self.assertFalse(prism.center)
        self.assertAlmostEqual(prism.height, 50.0)
        self.assertIsNone(prism.convexity)
        self.assertIsInstance(prism.extend_by_eps_sides, set)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(prism, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_smooth_prism_extend_by_eps(self):
        """
        Test a prism with top, some sides, and bottom extended by eps.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        nodes = [Vector2(0.0, 0.0),
                 Vector2(0.0, 60.0),
                 Vector2(60.0, 0.0)]

        prism = SmoothPrismHedron(height=50.0,
                                  points=nodes,
                                  profile_top=Fillet(radius=5.0),
                                  profile_verticals=Fillet(radius=5.0),
                                  profile_bottom=Chamfer(skew_length=5.0),
                                  extend_by_eps_top=True,
                                  extend_by_eps_sides=[False, True],
                                  extend_by_eps_bottom=True)

        self.assertFalse(prism.center)
        self.assertAlmostEqual(prism.height, 50.0)
        self.assertIsNone(prism.convexity)
        self.assertIsInstance(prism.extend_by_eps_sides, set)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(prism, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_smooth_prism_external_profile_bottom(self):
        """
        Test a prism with an external profile at the bottom.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        points = [Vector2.origin,
                  Vector2(0.0, 200.0),
                  Vector2(200.0, 200.0),
                  Vector2(200.0, 100.0),
                  Vector2(100.0, 125.0),
                  Vector2(100.0, 50.0)]

        prism = SmoothPrismHedron(height=100.0,
                                  points=points,
                                  profile_top=Fillet(radius=10.0),
                                  profile_verticals=Fillet(radius=10.0),
                                  profile_bottom=Chamfer(skew_length=10.0, side=2),
                                  extend_by_eps_top=True,
                                  extend_by_eps_bottom=True,
                                  extend_by_eps_sides=[True])

        self.assertFalse(prism.center)
        self.assertAlmostEqual(prism.height, 100.0)
        self.assertIsNone(prism.convexity)
        self.assertIsInstance(prism.extend_by_eps_sides, set)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(prism, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_smooth_prism_external_profile_top(self):
        """
        Test a prism with an external profile at the top.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        points = [Vector2.origin,
                  Vector2(0.0, 200.0),
                  Vector2(200.0, 200.0),
                  Vector2(200.0, 100.0),
                  Vector2(100.0, 125.0),
                  Vector2(100.0, 50.0)]

        prism = SmoothPrismHedron(height=100.0,
                                  points=points,
                                  profile_top=Fillet(radius=10.0, side=1),
                                  profile_verticals=Fillet(radius=10.0),
                                  profile_bottom=Chamfer(skew_length=10.0),
                                  extend_by_eps_top=True,
                                  extend_by_eps_bottom=True,
                                  extend_by_eps_sides=[True])

        self.assertFalse(prism.center)
        self.assertAlmostEqual(prism.height, 100.0)
        self.assertIsNone(prism.convexity)
        self.assertIsInstance(prism.extend_by_eps_sides, set)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(prism, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_smooth_prism_external_profile_other_sides(self):
        """
        Test a prism with an external profiles at the top and bottom.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        points = [Vector2.origin,
                  Vector2(0.0, 200.0),
                  Vector2(200.0, 200.0),
                  Vector2(200.0, 100.0),
                  Vector2(100.0, 125.0),
                  Vector2(100.0, 50.0)]

        prism = SmoothPrismHedron(height=100.0,
                                  points=points,
                                  profile_top=Fillet(radius=10.0, side=2),
                                  profile_verticals=Fillet(radius=10.0),
                                  profile_bottom=Chamfer(skew_length=10.0, side=1),
                                  extend_by_eps_top=True,
                                  extend_by_eps_bottom=True,
                                  extend_by_eps_sides=[True])

        self.assertFalse(prism.center)
        self.assertAlmostEqual(prism.height, 100.0)
        self.assertIsNone(prism.convexity)
        self.assertIsInstance(prism.extend_by_eps_sides, set)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(prism, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_anti_clockwise(self):
        """
        Test an anti-clockwise prism.
        """
        context = Context(eps=2.0)
        scad = Scad(context=context)

        nodes = [Vector2(0.0, 0.0),
                 Vector2(0.0, 60.0),
                 Vector2(60.0, 0.0)]
        nodes.reverse()

        prism = SmoothPrismHedron(height=50.0, points=nodes)

        self.assertRaises(ValueError, lambda: scad.run_super_scad(prism, 'demo.scad'))

# ----------------------------------------------------------------------------------------------------------------------
