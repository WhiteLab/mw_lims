import django.utils.timezone
from django.db import models


class Individuals(models.Model):
    individual_id = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)


class Samples(models.Model):
    sample_id = models.CharField(20)
    date_obtained = models.DateField(default=django.utils.timezone.now)
    tissue = models.CharField(45)
    individual_id = models.ForeignKey(to_field=Individuals, rel_class='ManyToOneRel')


class SampleAliquot(models.Model):
    sample_aliquot_id = models.CharField(max_length=20)
    date = models.DateField(default=django.utils.timezone.now)
    technician = models.CharField(max_length=45)
    concentration = models.CharField(max_length=45)
    sample_id = models.ForeignKey(Samples)


class Antibodies(models.Model):
    antibody_id = models.CharField(max_length=10)
    company = models.CharField(max_length=45)
    weight = models.FloatField(max_length=10)
    target = models.CharField(max_length=45)


class AntibodyAliquot(models.Model):
    antibody_aliquot_id = models.CharField(max_length=20)
    date_received = models.DateField(default=django.utils.timezone.now)
    antibody_id = models.ForeignKey(to_field=Antibodies, rel_class='ManyToOneRel')


class ExperimentDetails(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    duration = models.CharField(max_length=45)
    pipetting = models.CharField(max_length=45)
    gels = models.CharField(max_length=45)
    electrophoresis = models.CharField(max_length=45)
    transfer = models.CharField(max_length=45)
    image_id = models.CharField(max_length=45)
    image = models.BinaryField
    comments = models.TextField(max_length=250)
    sample_id = models.ForeignKey(Samples)


class ExperimentResults(models.Model):
    spot_id = models.CharField(max_length=10)
    raw_signal = models.FloatField(max_length=10)
    bg_signal = models.FloatField(max_length=10)
    bg_corrected_signal = models.FloatField(max_length=10)
    trimmed_signal = models.FloatField(max_length=10)
    signal_to_noise_ratio = models.FloatField(max_length=10)
    spot_area = models.FloatField(max_length=10)
    nano_droplet_velocity = models.FloatField(max_length=10)
    nano_droplet_volume = models.FloatField(max_length=10)
    spot_problem = models.CharField(max_length=1)
    comments = models.TextField(max_length=250)
    experiment_id = models.ForeignKey(to_field=ExperimentDetails, rel_class='ManyToOneRel')
    antibody_aliquot_id = models.ForeignKey(to_field=AntibodyAliquot)
    sample_id = models.ForeignKey(to_field=SampleAliquot, rel_class='ManyToOneRel')
