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
        'General Construction Services': 'images/General construction.jfif',
        'Design & Planning': 'images/design work.jpg',
        'Project Management': 'images/cart-excavator.jpg',
        'Renovation & Remodeling': 'images/renovation work.jfif',
        'Civil & Infrastructure Works': 'images/civil and infrustructure works.webp',
        'Mechanical, Electrical & Plumbing (MEP)': 'images/design, mechanical and electrical works.jfif',
        'Landscaping & External Works': 'images/landscaping work.webp',
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
        return 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=900&q=80'


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
        if self.photo and getattr(self.photo, 'url', None):
            return self.photo.url
        fallback = self.TEAM_PHOTO_MAP.get(self.name)
        if fallback:
            return f"{settings.STATIC_URL}{fallback}"
        return 'https://images.unsplash.com/photo-1544723795-3fb6469f5b39?auto=format&fit=crop&w=900&q=80'


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
            return 'https://images.unsplash.com/photo-1516455590571-18256e5bb9ff?auto=format&fit=crop&w=900&q=80'
        if 'tipper' in name or 'truck' in name:
            return 'https://images.unsplash.com/photo-1519821172141-bd363f66d472?auto=format&fit=crop&w=900&q=80'
        if 'mixer' in name or 'concrete' in name:
            return 'https://images.unsplash.com/photo-1504215680853-026ed2a45def?auto=format&fit=crop&w=900&q=80'
        if 'compactor' in name or 'roller' in name:
            return 'https://images.unsplash.com/photo-1556761175-587f7f8bd87e?auto=format&fit=crop&w=900&q=80'
        if 'crane' in name:
            return 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80'
        if 'generator' in name:
            return 'https://images.unsplash.com/photo-1515394771230-1b72e77f0b95?auto=format&fit=crop&w=900&q=80'
        if 'water' in name or 'bowser' in name or 'tanker' in name:
            return 'https://images.unsplash.com/photo-1581093588401-5a13f6f69988?auto=format&fit=crop&w=900&q=80'
        if 'welding' in name:
            return 'https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=900&q=80'
        return 'https://images.unsplash.com/photo-1516455590571-18256e5bb9ff?auto=format&fit=crop&w=900&q=80'


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