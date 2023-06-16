import csv
import os


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
    'skin_wet',
    ]


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
