0x19-postmortem
This postmortem outlines the incident, our response, and the steps taken to prevent future occurrences. It serves as a learning experience to strengthen our system's resilience and improve our incident response capabilities.
In details
# Postmortem for Web Stack Debugging Outage: When APIs Play Hide and Seek

## Issue Summary:

**Duration:**  
Start Time: January 15, 2024, 14:30 UTC  
End Time: January 15, 2024, 16:45 UTC  

**Impact:**  
The main web application experienced a downtime of approximately 2 hours. Users encountered slow response times, and 30% of the user base was affected.

**Root Cause:**  
The web stack took an unexpected detour into chaos town due to an incorrect API address in the profile – like a GPS sending you to the wrong party!

## Timeline:

- **Detection:**  
  Detected at 14:30 UTC through automated monitoring alerts indicating high latency. Our systems felt a bit sluggish and sent us a passive-aggressive alert like, "Hey, things are not okay!"

- **Actions Taken:**  
  - Investigated database servers for performance issues, but it was like searching for a needle in a haystack.
  - Assumed database queries were the primary cause due to recent code changes. Our Sherlock Holmes hats were on – "The case of the mysteriously slow database!"
  - Realized the API address on the user profile was incorrect – a wild goose chase in the wrong direction!

- **Misleading Paths:**  
  - Investigated application server logs for errors, assuming the issue was in the application layer. The logs looked more like a novel than a clue.
  - Considered potential DDoS attacks, leading to unnecessary network analysis. Turns out, we were more likely victims of our marketing success than a cyber attack.

- **Escalation:**  
  - Escalated the incident to the Database Administration team because, well, it was their party, and we weren’t invited.
  - Informed senior engineers about the ongoing outage. Picture us blowing the emergency party horns – "Houston, we've got a problem!"

- **Resolution:**  
  Identified the incorrect API address on the user profile. It was like finding Waldo in a sea of pixels. Updated the API address on the profile, and the web stack got back on track – GPS recalibrated!

## Root Cause and Resolution:

**Root Cause:**  
Incorrect API address in the user profile led to failed API calls, causing a traffic jam in the web stack.

**Resolution:**  
Updated the user profile with the correct API address. No more wrong turns for our web stack!

## Corrective and Preventative Measures:

**Improvements:**  
- Implement additional validation checks for API addresses in user profiles. We're adding GPS verification!
- Enhance monitoring capabilities to detect inconsistencies in API addresses. Our scripts are getting a promotion to detective status.
- Conduct regular checks on user profiles for accurate API information. It's time for a profile spring cleaning!

**Tasks:**  
1. Add validation checks for API addresses during user profile updates. Let's prevent wrong addresses from sneaking in.
2. Enhance monitoring scripts to alert on incorrect API addresses. No more playing hide and seek!
3. Schedule periodic checks to ensure API addresses in user profiles are up to date. We're keeping our profiles in top shape!

## Conclusion:

This postmortem takes you on a journey of a web stack gone astray, all because of an innocent but incorrect API address. We fixed it, updated the GPS coordinates, and now our web stack is cruising smoothly again. This incident serves as a reminder to enhance our systems and implement preventive measures to avoid future detours.


Blog link
https://ruova.hashnode.dev/postmortem-for-web-stack-debugging-outage
