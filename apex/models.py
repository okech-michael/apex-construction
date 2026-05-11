from django.db import models


from django.conf import settings


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class e.g. fa-hard-hat")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    SERVICE_IMAGE_MAP = {
        'General Construction Services': 'images/general-construction.jfif',
        'Design & Planning': 'images/design-work.jpg',
        'Project Management': 'images/cart-excavator.jpg',
        'Renovation & Remodeling': 'images/renovation-work.jfif',
        'Civil & Infrastructure Works': 'images/civil-and-infrastructure-works.webp',
        'Mechanical, Electrical & Plumbing (MEP)': 'images/design-mechanical-electrical-works.jfif',
        'Landscaping & External Works': 'images/landscaping-work.webp',
    }

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and getattr(self.image, 'url', None):
            return self.image.url
        fallback = self.SERVICE_IMAGE_MAP.get(self.title)
        if fallback:
            return f"{settings.STATIC_URL}{fallback}"
        return f"{settings.STATIC_URL}images/general-construction.jfif"


class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('upcoming', 'Upcoming'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    location = models.CharField(max_length=200, blank=True)
    year = models.CharField(max_length=10, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    TEAM_PHOTO_MAP = {
        "Felix Ochieng'": 'images/team/felix-ochieng.jpeg',
        'Maxwell Okoth': 'images/team/maxwell.jfif',
        'Samuel Oketch': 'images/team/samuel.jpeg',
        'Mike Onyango': 'images/team/mica.png',
        'Reagan Obondo': 'images/team/reagan-obondo.jpg',
        'Ronex': 'images/team/ronex.jfif',
        'Richard': 'images/team/richard.jpg',
    }

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} – {self.role}"

    @property
    def photo_url(self):
        fallback = self.TEAM_PHOTO_MAP.get(self.name)
        if fallback:
            return f"{settings.STATIC_URL}{fallback}"
        if self.photo and getattr(self.photo, 'url', None):
            return self.photo.url
        return f"{settings.STATIC_URL}images/team/maxwell.jfif"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    client_role = models.CharField(max_length=200, blank=True)
    client_company = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} – Testimonial"


class MachineHire(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='machines/', blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, help_text="e.g. KES 15,000/day")
    is_available = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and self.image.name:
            try:
                if self.image.storage.exists(self.image.name):
                    return self.image.url
            except Exception:
                pass

        name = self.name.lower()
        if 'excavator' in name:
            return f"{settings.STATIC_URL}images/cart-excavator.jpg"
        if 'tipper' in name or 'truck' in name:
            return f"{settings.STATIC_URL}images/tipper-truck.jfif"
        if 'mixer' in name or 'concrete' in name:
            return f"{settings.STATIC_URL}images/concrete-mixer.jfif"
        if 'compactor' in name or 'roller' in name:
            return f"{settings.STATIC_URL}images/compactor-roler.jfif"
        if 'crane' in name:
            return f"{settings.STATIC_URL}images/tower-crane.jpg"
        if 'generator' in name:
            return f"{settings.STATIC_URL}images/GEnerator-vibrator.jfif"
        if 'water' in name or 'bowser' in name or 'tanker' in name:
            return f"{settings.STATIC_URL}images/water-bowser.jfif"
        if 'welding' in name:
            return f"{settings.STATIC_URL}images/welding-machine.jfif"
        return f"{settings.STATIC_URL}images/general-construction.jfif"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} – {self.created_at.strftime('%d %b %Y')}"


class ConsultationBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_interest = models.CharField(max_length=200, blank=True)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking – {self.name} on {self.preferred_date}"