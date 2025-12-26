# Requirements Document

## Introduction

This document outlines the requirements for system improvements and new features for the Iranian Pediatric Pulmonology Society (ISPP) website. The improvements include database connection reliability, new doctor resources page, publications updates, navigation changes, and a membership approval system.

## Glossary

- **System**: The ISPP website consisting of Django backend and Vue.js frontend
- **Database_Connection**: The connection between Django backend and the database
- **Doctors_Page**: A new page providing categorized resources for medical professionals
- **Publications_Page**: The existing publications page that needs updating with new categories
- **Membership_System**: The user registration and approval workflow
- **Admin_User**: A user with administrative privileges who can approve/reject membership requests
- **Pending_Member**: A registered user awaiting admin approval (is_active=False)
- **Content_API**: Backend API endpoints for serving file listings and content

## Requirements

### Requirement 1: Database Connection Reliability

**User Story:** As a system administrator, I want reliable database connections with automatic retry logic, so that temporary connection issues don't cause system failures.

#### Acceptance Criteria

1. WHEN a database connection fails, THE System SHALL retry the connection up to 3 times with exponential backoff
2. WHEN database connection timeout occurs, THE System SHALL handle it gracefully and return appropriate error messages
3. THE System SHALL implement connection pooling with CONN_MAX_AGE configuration
4. WHEN connection retry attempts are exhausted, THE System SHALL log the error and return a user-friendly error page
5. THE Database_Connection SHALL include timeout options in database configuration

### Requirement 2: Doctors Resource Page

**User Story:** As a medical professional, I want to access categorized educational resources, so that I can find relevant materials for my practice and education.

#### Acceptance Criteria

1. WHEN a user navigates to /doctors, THE System SHALL display a page with six resource categories
2. THE Doctors_Page SHALL include categories: SkyRoom, Video, Slides, Books, Brochures, and Documents
3. WHEN a user clicks on Books category, THE System SHALL display content from Content/Books/ directory with subdirectories
4. WHEN a user clicks on Brochures category, THE System SHALL display content from Content/Broshour/ directory
5. THE Content_API SHALL provide file listings for each category via GET /api/doctors/files/ endpoint
6. WHEN a user clicks on a file, THE System SHALL allow direct download or viewing of the resource
7. THE System SHALL display each category as clickable cards with appropriate icons and descriptions

### Requirement 3: Publications Page Updates

**User Story:** As a website visitor, I want to access updated publication categories, so that I can find relevant research and educational materials.

#### Acceptance Criteria

1. THE Publications_Page SHALL display five main categories: Newsletters, Congress Booklets, Association Journal, Other Products, and Research
2. WHEN a user clicks on Association Journal, THE System SHALL redirect to https://brieflands.com/journals/jcp
3. THE Publications_Page SHALL display each category as cards with download/access capabilities
4. WHEN categories contain files, THE System SHALL provide direct access to download them
5. THE Publications_Page SHALL maintain responsive design across all device sizes

### Requirement 4: Navigation Simplification

**User Story:** As a website visitor, I want a simplified navigation menu, so that I can focus on relevant content without unnecessary language options.

#### Acceptance Criteria

1. THE System SHALL remove the English language link from the main navigation bar
2. THE System SHALL maintain all other existing navigation links and functionality
3. WHEN the English link is removed, THE System SHALL preserve the overall navigation layout and styling

### Requirement 5: Membership Approval System

**User Story:** As an administrator, I want to review and approve membership requests, so that I can control who gains access to the system.

#### Acceptance Criteria

1. WHEN a new user registers, THE Membership_System SHALL create the user with is_active=False status
2. WHEN a user registers, THE System SHALL display a message indicating their request is pending admin approval
3. WHEN a user registers, THE System SHALL NOT automatically log them in
4. THE System SHALL provide an API endpoint GET /api/members/pending/ to list all Pending_Members
5. THE System SHALL provide an API endpoint POST /api/members/{user_id}/approve/ to approve a Pending_Member
6. THE System SHALL provide an API endpoint POST /api/members/{user_id}/reject/ to reject a Pending_Member
7. WHEN an Admin_User approves a member, THE System SHALL set is_active=True for that user
8. WHEN an Admin_User rejects a member, THE System SHALL either delete the user or mark them as rejected
9. THE System SHALL add a "Membership Requests" tab to the login modal for new user registration
10. THE System SHALL add a "Membership Requests" management tab to the admin dashboard
11. WHEN displaying pending requests, THE System SHALL show user details and provide approve/reject buttons

### Requirement 6: Content File Management

**User Story:** As a system, I want to efficiently serve file listings from content directories, so that users can access educational materials through the doctors page.

#### Acceptance Criteria

1. THE Content_API SHALL read directory structure from frontend/public/Content/Books/ and frontend/public/Content/Broshour/
2. WHEN reading directories, THE Content_API SHALL support nested subdirectories for Books category
3. THE Content_API SHALL return file metadata including name, size, and file type
4. WHEN a directory is empty, THE Content_API SHALL return an empty list without errors
5. THE Content_API SHALL filter files by category parameter (books, brochures, slides, videos, documents)
6. THE Content_API SHALL handle file access permissions and return appropriate error messages for inaccessible files

### Requirement 7: User Interface Integration

**User Story:** As a website visitor, I want seamless integration of new features with existing UI, so that the user experience remains consistent and intuitive.

#### Acceptance Criteria

1. THE System SHALL add "Doctors" link to the main navigation bar
2. THE System SHALL integrate the membership request form into the existing login modal
3. WHEN admin users access the dashboard, THE System SHALL display the membership management tab only for authorized users
4. THE System SHALL maintain consistent styling and theming across all new pages and components
5. THE System SHALL ensure all new UI elements are responsive and work on mobile devices