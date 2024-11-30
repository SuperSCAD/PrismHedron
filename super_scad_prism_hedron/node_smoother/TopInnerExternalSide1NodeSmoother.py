import math
from typing import List

from super_scad.type import Vector2, Vector3

from super_scad_prism_hedron.node_smoother.NodeSmoother import NodeSmoother


class TopInnerExternalSide1NodeSmoother(NodeSmoother):
    """
    Class for smooth a node with an inner corner and external profile at side 1 add the top of the prism.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def create_layers(self,
                      height: float,
                      inner_angle: float,
                      normal_angle: float,
                      points_vertical: List[Vector2],
                      points_horizontal: List[Vector2]) -> List[List[Vector3]]:
        """
        Creates layers that smooth the node.

        :param height: The height of the node.
        :param inner_angle: The inner angle of the node.
        :param normal_angle: The normal angle of the node.
        :param points_vertical: The points of the vertical profiles at the node.
        :param points_horizontal: The points of the two horizontal profiles at the node.
        """
        layers = []
        alpha = math.radians(0.5 * inner_angle)
        for index_h in range(len(points_horizontal) - 1, -1, -1):
            layer = []
            z = height + points_horizontal[index_h].y
            for index_v in range(len(points_vertical)):
                length = (points_horizontal[index_h].x - points_horizontal[-1].x) / math.sin(alpha)
                point = points_vertical[index_v] + Vector2.from_polar_coordinates(length, normal_angle)
                layer.append(Vector3(point.x, point.y, z))
            layers.append(layer)

        return layers

# ----------------------------------------------------------------------------------------------------------------------
