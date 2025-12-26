# Design Document: System Improvements and New Features

## Overview

This design document outlines the implementation approach for enhancing the ISPP website with improved database reliability, new doctor resources functionality, updated publications, simplified navigation, and a comprehensive membership approval system. The solution maintains the existing Django/Vue.js architecture while adding robust error handling, new API endpoints, and enhanced user management capabilities.

## Architecture

The system follows a three-tier architecture:

### Frontend Layer (Vue.js)
- **New Components**: Doctors.vue page, membership request forms, admin management interface
- **Updated Components**: App.vue navigation, Publications.vue categories, Dashboard.vue admin tabs
- **API Integration**: Axios-based HTTP client for backend communication

### Backend Layer (Django)
- **New Apps**: `doctors` app for resource management
- **Enhanced Apps**: `accounts` app with membership approval workflow
- **Middleware**: Database connection retry and timeout handling
- **API Endpoints**: RESTful APIs for file management and user approval

### Data Layer
- **Database**: Enhanced connection pooling and retry logic
- **File System**: Structured content directory management
- **Static Files**: Organized resource categories in public/Content/

## Components and Interfaces

### 1. Database Connection Enhancement

#### Middleware Component
```python
class DatabaseRetryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_retries = 3
        self.base_delay = 1.0
    
    def __call__(self, request):
        # Retry logic with exponential backoff
        # Timeout handling
        # Error logging and user-friendly responses
```

#### Settings Configuration
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'CONN_MAX_AGE': 600,  # Connection pooling
        'OPTIONS': {
            'connect_timeout': 10,
            'command_timeout': 30,
        }
    }
}
```

### 2. Doctors Resource Management

#### Backend API Interface
```python
# doctors/views.py
class DoctorsFileListView(APIView):
    def get(self, request):
        category = request.GET.get('category', 'all')
        # Returns structured file listings
        
class FileDownloadView(APIView):
    def get(self, request, file_path):
        # Secure file serving with access control
```

#### Frontend Component Interface
```vue
<!-- Doctors.vue -->
<template>
  <div class="doctors-page">
    <div class="category-grid">
      <CategoryCard 
        v-for="category in categories" 
        :key="category.id"
        :category="category"
        @click="loadCategoryFiles"
      />
    </div>
    <FileList 
      :files="currentFiles"
      @download="handleFileDownload"
    />
  </div>
</template>
```

### 3. Membership Approval System

#### Backend Models Enhancement
```python
# accounts/models.py
class CustomUser(AbstractUser):
    # Existing fields...
    approval_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
```

#### API Endpoints
```python
# accounts/views.py
class PendingMembersView(APIView):
    permission_classes = [IsAdminUser]
    
class ApproveMemberView(APIView):
    permission_classes = [IsAdminUser]
    
class RejectMemberView(APIView):
    permission_classes = [IsAdminUser]
```

#### Frontend Integration
```vue
<!-- Dashboard.vue - Admin Tab -->
<template>
  <div class="membership-management">
    <MembershipRequestList 
      :pending-requests="pendingRequests"
      @approve="approveMember"
      @reject="rejectMember"
    />
  </div>
</template>
```

## Data Models

### Enhanced User Model
```python
class CustomUser(AbstractUser):
    # Existing profile fields
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
    experience = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    
    # New approval workflow fields
    approval_status = models.CharField(max_length=20, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    rejection_reason = models.TextField(blank=True)
```

### File Management Models
```python
class ResourceCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    directory_path = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)
    description = models.TextField()

class ResourceFile(models.Model):
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=500)
    file_size = models.BigIntegerField()
    file_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
```

## Error Handling

### Database Connection Errors
- **Retry Logic**: Exponential backoff with maximum 3 attempts
- **Timeout Handling**: Configurable connection and command timeouts
- **Graceful Degradation**: User-friendly error pages for persistent failures
- **Logging**: Comprehensive error logging for debugging

### File Access Errors
- **Permission Checks**: Validate file access before serving
- **Path Validation**: Prevent directory traversal attacks
- **Missing Files**: Return appropriate 404 responses
- **Large Files**: Streaming responses for large file downloads

### API Error Responses
```python
{
    "error": {
        "code": "DATABASE_CONNECTION_FAILED",
        "message": "Service temporarily unavailable. Please try again later.",
        "details": "Connection timeout after 3 retry attempts"
    }
}
```

## Testing Strategy

### Unit Testing Approach
- **Django Tests**: Test database middleware, API endpoints, and model methods
- **Vue Component Tests**: Test component rendering, user interactions, and API integration
- **Integration Tests**: Test complete workflows from frontend to backend
- **File System Tests**: Test directory reading and file serving functionality

### Property-Based Testing Configuration
- **Framework**: Django's built-in testing framework with Hypothesis for property-based tests
- **Test Configuration**: Minimum 100 iterations per property test
- **Coverage**: Focus on API endpoints, user workflows, and file management operations

### Dual Testing Strategy
- **Unit Tests**: Verify specific examples, edge cases, and error conditions
- **Property Tests**: Verify universal properties across all inputs
- Both approaches are complementary and necessary for comprehensive coverage

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Database Connection Retry Behavior
*For any* database connection failure, the system should retry exactly 3 times with exponential backoff timing between attempts
**Validates: Requirements 1.1**

### Property 2: Database Timeout Handling
*For any* database connection timeout scenario, the system should handle it gracefully and return appropriate error messages without crashing
**Validates: Requirements 1.2**

### Property 3: Retry Exhaustion Logging
*For any* database connection failure where all retry attempts are exhausted, the system should log the error and return a user-friendly error page
**Validates: Requirements 1.4**

### Property 4: Directory Content Reading
*For any* valid directory path (Books or Brochures), when a user requests category content, the system should return all files from that directory including subdirectories
**Validates: Requirements 2.3, 2.4**

### Property 5: Content API File Listings
*For any* category parameter provided to the Content API, the system should return appropriate file listings for that category
**Validates: Requirements 2.5**

### Property 6: File Download Access
*For any* accessible file in the content directories, when a user requests download, the system should serve the file successfully
**Validates: Requirements 2.6**

### Property 7: Publications File Access
*For any* category containing files on the Publications page, the system should provide direct download access to those files
**Validates: Requirements 3.4**

### Property 8: Navigation Link Preservation
*For any* existing navigation link (except English), the system should maintain the link's functionality after removing the English link
**Validates: Requirements 4.2**

### Property 9: User Registration Status
*For any* new user registration, the system should create the user with is_active=False status
**Validates: Requirements 5.1**

### Property 10: Registration Pending Message
*For any* user registration attempt, the system should display a pending approval message
**Validates: Requirements 5.2**

### Property 11: Registration Auto-Login Prevention
*For any* user registration, the system should not automatically log the user in
**Validates: Requirements 5.3**

### Property 12: Pending Members API
*For any* request to the pending members API endpoint, the system should return all users with is_active=False status
**Validates: Requirements 5.4**

### Property 13: Member Approval API
*For any* valid user ID provided to the approval API, the system should set that user's is_active status to True
**Validates: Requirements 5.5**

### Property 14: Member Rejection API
*For any* valid user ID provided to the rejection API, the system should either delete the user or mark them as rejected
**Validates: Requirements 5.6**

### Property 15: Admin Approval Behavior
*For any* pending member approved by an admin user, the system should set is_active=True for that member
**Validates: Requirements 5.7**

### Property 16: Admin Rejection Behavior
*For any* pending member rejected by an admin user, the system should either delete the user or mark them as rejected
**Validates: Requirements 5.8**

### Property 17: Content Directory Structure Reading
*For any* content directory (Books or Brochures), the Content API should correctly read and return the directory structure
**Validates: Requirements 6.1**

### Property 18: Nested Directory Support
*For any* nested subdirectory in the Books category, the Content API should include files from all nested levels
**Validates: Requirements 6.2**

### Property 19: File Metadata Extraction
*For any* file in the content directories, the Content API should return metadata including name, size, and file type
**Validates: Requirements 6.3**

### Property 20: Category Filtering
*For any* category filter parameter (books, brochures, slides, videos, documents), the Content API should return only files matching that category
**Validates: Requirements 6.5**

### Property 21: File Permission Error Handling
*For any* inaccessible file due to permissions, the Content API should return appropriate error messages
**Validates: Requirements 6.6**

### Property 22: Admin Dashboard Authorization
*For any* user accessing the dashboard, the membership management tab should only be visible to users with admin privileges
**Validates: Requirements 7.3**