## Action Points from Meeting Transcript:

**I.  UI/UX Changes:**

* **A. Additional Services Section:** Create a new section for "Additional Services" as a third step in the booking process, *after* choosing optional courses.  This section will display services as tiles (2-3 per row) showcasing available options for the selected menu.
    *  **Detail:**  The tiles should include a picture of the service, a description of what's included, and the total price (calculated based on price per person and number of guests).  Remove unnecessary elements from the current design.  An "Add" or "Exit" button should be included in the quick view.
* **B. Menu Page Updates:** Integrate the additional services section seamlessly into the existing menu pages.


**II. Backend Development:**

* **A. Chef Functionality:**
    *  Allow chefs to add additional services to their menus. This will be located within the menu creation/editing section, similar to adding a kids' menu.
    *  Provide a dropdown menu for selecting pre-existing additional services (created by admin).
    *  Chefs will input the price per person for each selected service.  They cannot create new service types; only select from pre-existing options.
* **B. Admin Functionality:**
    *  Create a dedicated section for managing additional services.
    *  This section will allow admins to add new services, including:
        * Service Name
        * Description
        * Slug
        * Image (to be automatically tied to the service)
        * Status
        * Option to designate if service is "Chef Demanded" (no service area or price set by admin; price set by chef) or "FFK/Service Provider Provided" (requires service area and price set by admin).
    *  Set pricing for "FFK/Service Provider Provided" services.
* **C. Service Provider Functionality:**
    *  Create a new user type: "Service Provider".
    *  Service providers will have a profile section to input:
        * Company Name
        * Phone Number
        * Email
        * Address
        * Bio
        * Service Area (radius)
        * Stripe Account Connection
        * Vendor Agreement Acceptance
    *  Service providers will be able to:
        * Add their own additional services (with description, image, and pricing).
        * View their bookings, including:  chef, menu, date, time, guest contact info, special instructions, and estimated payout.
    *   Service providers will manage their own availability, potentially integrating with Google Calendar in a future iteration.
* **D.  Location-Based Logic:**
    *  Implement location-based logic to ensure additional services only appear for menus within the service provider's or chef's service radius.  This applies to both chef-provided and service provider-offered services.
    *  If a chef operates in multiple areas, additional services should only show for menus within the specified area of the booking.


**III. Research & Planning:**

* **A. Calendar Integration:** Research and determine which calendar systems (e.g., Google Calendar) to integrate for availability management.  Potentially survey chefs to gauge preferred calendar systems. This will be addressed in a future meeting.
* **B. Service Provider Details:**  Document the complete functionality and design for the service provider dashboard and booking details.  This will include creating a design and a document. This will be addressed in a future meeting.

**IV.  Meeting Follow-Up:**

* Schedule a follow-up meeting to discuss the completed documentation and design for service provider functionality and address any remaining questions.