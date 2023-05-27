import csv
import os

import numpy as np


SUPPORTED_TISSUES = [
    'air',
    'blood',
    'blood_vessel',
    'body_fluid',
    'bone_cancellous',
    'bone_cortical',
    'bone_marrow',
    'brain_grey_matter',
    'brain_white_matter',
    'cerebellum',
    'cerebro_spinal_fluid',
    'dura', 'fat',
    'muscle',
    'skin_dry',
    'skin_wet'
    ]
SUPPORTED_POLARIZATIONS = ['parallel', 'orthogonal']
SUPPORTED_LIMITS = ['icnirp', 'ieee']
SUPPORTED_EXPOSURE = ['occupational', 'general public']


def load_tissue_properties(tissue, frequency):
    """Return conductivity, relative permitivity, loss tangent and
    penetration depth of a given tissue based on a given frequency.
    
    Parameters
    ----------
    tissue : str
        type of human tissue
    frequency : float
        radiation frequency
        
    Returns
    -------
    tuple
        Values for conductivity, relative permitivity, loss tangent and
        penetration depth of a given tissue at corresponding frequency.
    """
    tissue = tissue.lower()
    if tissue not in SUPPORTED_TISSUES:
        raise ValueError(
            f'Unsupported tissue. Choose from: {SUPPORTED_TISSUES}.'
            )
    if 1e9 > frequency > 100e9:
        raise ValueError('Invalid frequency. Choose in [1, 100] GHz range.')
    fname = os.path.join('data', 'tissue_properties.csv')
    with open(fname) as f:
        reader = csv.reader(f)
        for row in reader:
            if str(row[0]) == tissue and float(row[1]) == frequency:
                conductivity = float(row[2])
                relative_permitivity = float(row[3])
                loss_tangent = float(row[4])
                penetration_depth = float(row[5])
    return conductivity, relative_permitivity, loss_tangent, penetration_depth


def reflection_coefficient(eps, angle=0, polarization='parallel'):
    """Return reflection coefficient for oblique plane wave incidence.
    
    Parameters
    ----------
    eps : float
        Relative permittivity.
    angle : float
        angle of incidence in degrees.
    polarization : str
        Either parallel or orthogonal polarization.
    
    Returns
    -------
    float
        Reflection coefficient.
    """
    polarization = polarization.lower()
    if polarization not in SUPPORTED_POLARIZATIONS:
        raise ValueError(
            f'Unsupported tissue. Choose from: {SUPPORTED_POLARIZATIONS}.'
        )
    scaler = np.sqrt(eps - np.sin(angle) ** 2)
    if polarization == 'parallel':
        gamma = ((-eps * np.cos(angle) + scaler)
                 / (eps * np.cos(angle) + scaler))
    elif polarization == 'orthogonal':
        gamma = ((np.cos(angle) - scaler)
                 / (np.cos(angle) + scaler))
    else:
        pass
    return gamma


def incident_power_density(frequency, limits, exposure):
    """Return inciden power density value at a given frequency.
    
    Parameters
    ----------
    frequency : float
        Frequency at the 6-300 GHz range.
    limits : str
        Supported exposure limits are: 'icnirp' and 'ieee'.
    exposure: str
        Supported exposure scenarios are 'occupational' and
        'general public'.

    Returns
    -------
    float
        Incident power density, either peak or spatially averaged.
    """
    if (frequency < 6e9) | (frequency > 300e9):
        raise ValueError('Frequency out of the supported range.')
    limits = limits.lower()
    assert limits in SUPPORTED_LIMITS, 'Limits not supported.'
    exposure = exposure.lower()
    assert exposure in SUPPORTED_EXPOSURE, 'Exposure not supported.'
    exposure = exposure.lower()
    if frequency == 6e9:
        if exposure == 'occupational':
            return 200
        return 40
    elif 6e9 < frequency < 300e9:
        if exposure == 'occupational':
            if limits == 'icnirp':
                return 275 * (frequency / 1e9) ** (-0.177)
            return 274.8 * (frequency / 1e9) ** (-0.177)
        return 55 * (frequency / 1e9) ** (-0.177)
    if exposure == 'occupational':
        return 100
    return 20
