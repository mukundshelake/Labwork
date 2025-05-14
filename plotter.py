"""
plot_pcb_vs_sensor.py

This script plots the relative position and rotation of a PCB with respect to its sensor.
It is intended for QA/validation during module assembly.

Inputs:
- Relative X and Y shifts of the PCB with respect to the sensor (in mm)
- Relative angle (rotation) of the PCB with respect to the sensor (in degrees)

Output:
- A matplotlib plot showing:
  - PCB shifts in microns
  - PCB rotation on a radial gauge
  - Tolerance bands (±50 μm, ±100 μm for position; ±0.02°, ±0.04° for rotation)

Usage:
------
Modify the `if __name__ == "__main__":` section to define module name and values.
Run as:

    python plot_pcb_vs_sensor.py

Dependencies:
------------
- numpy
- matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def make_pcb_vs_sensor_plot(
    module_name='M01',
    rel_pcb_X=[0.020],    # mm
    rel_pcb_Y=[0.025],    # mm
    rel_pcb_angle=[-0.004]  # degrees
):
    """
    Generate a QA plot of PCB position and rotation w.r.t. sensor.

    Parameters
    ----------
    module_name : str
        Name of the module to use in the title and output filename.
    rel_pcb_X : list of float
        X offsets of PCB w.r.t. sensor in mm.
    rel_pcb_Y : list of float
        Y offsets of PCB w.r.t. sensor in mm.
    rel_pcb_angle : list of float
        Angular offset of PCB w.r.t. sensor in degrees.
    """

    fig, ax = plt.subplots(figsize=(6, 6), layout='constrained')
    ax.set_box_aspect(1)
    ax.set_title(f'{module_name} PCB vs Sensor', y=1.15, fontsize=20)

    # Convert mm → μm for display
    rel_pcb_X = np.array(rel_pcb_X) * 1000
    rel_pcb_Y = np.array(rel_pcb_Y) * 1000

    # --- Position Scatter Plot ---
    ax.scatter(rel_pcb_X, rel_pcb_Y, color='#2ca02c', label='PCB')
    ax.scatter([0.], [0.], color='k', label='Sensor (reference)')

    ax.set_xlabel('$\Delta x$ [$\mu m$]', fontsize=18)
    ax.set_ylabel('$\Delta y$ [$\mu m$]', fontsize=18)

    # Axis ticks and limits
    ax.set_xlim(-200, 300)
    ax.set_ylim(-200, 300)
    ax.xaxis.set_major_locator(MultipleLocator(100))
    ax.yaxis.set_major_locator(MultipleLocator(100))
    ax.xaxis.set_minor_locator(MultipleLocator(25))
    ax.yaxis.set_minor_locator(MultipleLocator(25))
    ax.grid(False)

    # Draw tolerance boxes
    ax.vlines([-50, 50], -50, 50, colors='b')
    ax.hlines([-50, 50], -50, 50, colors='b')
    ax.text(-70, 55, '50 $\mu m$', color='b', fontsize=12)

    ax.vlines([-100, 100], -100, 100, colors='r')
    ax.hlines([-100, 100], -100, 100, colors='r')
    ax.text(-100, 105, '100 $\mu m$', color='r', fontsize=12)

    # Reference lines at origin
    ax.axhline(0, color='k')
    ax.axvline(0, color='k')

    # Ticks style
    plt.tick_params(axis='both', which='minor', direction='in', labelsize=0, length=5, width=1, right=True, top=True)
    plt.tick_params(axis='both', which='major', direction='in', labelsize=18, length=7, width=1.5, right=True, top=True)

    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower right', ncol=2, borderaxespad=0.)

    # --- Rotation Gauge Plot ---
    ax_sub = fig.add_axes([.52, .58, .42, .25], polar=True)

    # Define gauge scale
    gauge_angle_max = 0.04     # max angle in deg (±0.04°)
    gauge_angle_unit = 0.02    # major tick spacing in deg

    transfer_factor = 40. / gauge_angle_max  # scaling for angle ticks
    orig_gauge_angle_unit = transfer_factor * gauge_angle_unit

    ax_sub.set_rmax(2)
    ax_sub.get_yaxis().set_visible(False)
    ax_sub.grid(False)

    ax_sub.set_theta_offset(np.pi / 2)
    ax_sub.set_thetamin(-40)
    ax_sub.set_thetamax(40)
    ax_sub.set_rorigin(-2.5)

    # Draw tick marks (minor and major)
    tick_minor = [ax_sub.get_rmax(), ax_sub.get_rmax() * 0.97]
    tick_major = [ax_sub.get_rmax(), ax_sub.get_rmax() * 0.9]

    for t in np.deg2rad(np.arange(0, 360, orig_gauge_angle_unit * 0.5)):
        ax_sub.plot([t, t], tick_minor, lw=0.72, color="k")

    for t in np.deg2rad(np.arange(0, 360, orig_gauge_angle_unit)):
        ax_sub.plot([t, t], tick_major, lw=0.72, color="k")

    # Set angular labels
    ax_sub.set_thetagrids(
        np.arange(40, -41, -orig_gauge_angle_unit),
        labels=np.round(np.arange(gauge_angle_max, -gauge_angle_max - gauge_angle_unit, -gauge_angle_unit), 2)
    )

    # Plot PCB angles
    for angle in rel_pcb_angle:
        ax_sub.annotate('', xy=(transfer_factor * angle * np.pi / 180., 2),
                        xytext=(0., -2.5),
                        arrowprops=dict(color='#2ca02c', arrowstyle="->"))

    # Reference sensor arrow
    ax_sub.annotate('', xy=(0., 2), xytext=(0., -2.5),
                    arrowprops=dict(color='k', arrowstyle="->"))

    # Tolerance lines (±0.02° and ±0.04°)
    for tol_angle, color in zip([0.02, -0.02], ['b', 'b']):
        ax_sub.annotate('', xy=(transfer_factor * tol_angle * np.pi / 180., 2),
                        xytext=(transfer_factor * tol_angle * np.pi / 180., 0.),
                        arrowprops=dict(color=color, arrowstyle="-", linestyle="dotted"))

    for tol_angle, color in zip([0.04, -0.04], ['r', 'r']):
        ax_sub.annotate('', xy=(transfer_factor * tol_angle * np.pi / 180., 2),
                        xytext=(transfer_factor * tol_angle * np.pi / 180., 0.),
                        arrowprops=dict(color=color, arrowstyle="-", linestyle="dotted"))

    # Save and display
    plt.savefig(f'{module_name}_pcb_vs_sensor.png')
    plt.show()
    plt.close()


if __name__ == "__main__":
    # Example input: For each hole, one can fill in these lists.
    make_pcb_vs_sensor_plot(
        module_name='M07',
        rel_pcb_X=[0.018, 0.022, 0.019],      # mm
        rel_pcb_Y=[0.027, 0.023, 0.026],      # mm
        rel_pcb_angle=[-0.004, -0.006, -0.005]  # degrees
    )

    
