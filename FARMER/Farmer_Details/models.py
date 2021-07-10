from django.db import models


class District(models.Model):
    district_name       = models.CharField(max_length=20)
    added_on            = models.DateTimeField()
    def __str__(self):
        return "%s" % (self.district_name)


class Taluka(models.Model):
    taluka_name         = models.CharField(max_length=20)
    district_id         = models.ForeignKey(District, on_delete=models.CASCADE)
    added_on            = models.DateTimeField()
    def __str__(self):
        return "%s" % (self.taluka_name)


class Village(models.Model):
    village_name        = models.CharField(max_length=20)
    taluka_id           = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    added_on            = models.DateTimeField()
    def __str__(self):
        return "%s" % (self.village_name)

class Farmer(models.Model):
    first_name          = models.CharField(max_length=30)
    middle_name         = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    mobile_number       = models.BigIntegerField()
    aadhaar_number      = models.BigIntegerField()
    district            = models.ForeignKey(District, on_delete=models.CASCADE)
    taluka              = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    village             = models.ForeignKey(Village, on_delete=models.CASCADE)
    address             = models.CharField(max_length=30)
    img_path            = models.CharField(max_length=50)
    added_on            = models.DateTimeField()
    farmer_active       = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

