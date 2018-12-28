
========
Personalization
========

Dyrii allows users to configure some of the features to make it more personal and specific to their needs. Both iOS and Mac apps have a Personalization section within the Settings Screen for this purpose. In this chapter, we will discuss some of the key personalization option in detail. 

Please note that these personalization options are stored locally in the given device and is not  synced across other devices or reapplied when app is deleted and reinstalled. 

Default Landing Screen
--------
While Dyrii comes with Timeline view set as the default Landing Screen view, this can be changed to Day View from Settings > Personalize > Default View.


Day Trails
------------
This feature tracks all the places you visit in a given day and draws it on a map view with pins indicating the places where you stopped over. This feature is turned off my default due to privacy reasons and need to be consciously turned on by the user from Settings > Personalization > Track Places Visited. This feature works by setting a geofence based on your current location and updating the geofence it when you move outside. Since the accuracy of the pins are based on the radius of the geofence, we have exposed the radius as an option that users can configure. 

Please note that selecting a smaller radius will consumer more battery power so pick a value based on your need and context. 

Passcode
----------
Dyrii comes with a passcode feature that can be used to block other members who may have access to your device from viewing your journal entries. Dyrii supports both strong alphanumeric password based locks as well as Apple’s Touch ID and Face ID based locks. While setting the passcode, please keep it in a safe place so that you can access it in case you forget it since we are be unable to reset the passcode for you. 

Note: The passcode protection is local to the device and the passcode does not sync across devices. 

iOS
To set passcode protection, navigate to Settings/Personalize/Passcode option and enable this option. 

Mac
On the mac, to enable this function, click on the lock button on the toolbar and pick a passcode. 

Reminders
-------
We understand journaling consistently every day can be tough. To help with this, we have included Reminders which can be set to recurring frequency.

.. image:: _images/reminder_frequency_ios.JPG
   :width: 300px
   :alt: alternate text

Favorities 
-------
As we discussed in previous chapter, Dyrii allows you to mark entries as favorites, which can then be viewed as a journal view under Menu screen. In addition, we have designed Favorites to serve as either 5-star rating based system or a binary flag based system. You can configure this behavior from Settings > Personalize > Use 5-stars for Favorites. The default option is set to behave as a binary flag based system. 

.. image:: _images/reminder_frequency_ios.JPG
   :width: 300px
   :alt: alternate text

First Day of Week
-------
In the previous chapter, we discussed how a weekly header strip is displayed in Day View. There the first day of the week is set to Sunday by default but this option can be changed to any day of the week. This option is located under Settings > Preference > First Day of the Week. This option also affects the behavior in the calendar view under Perspectives. 

.. image:: _images/reminder_frequency_ios.JPG
   :width: 300px
   :alt: alternate text

Metric Units
-------
Dyrii by default displays certain metadata values such as weather, time, distance in Imperial system. Users located in regions where metric system is used can change this behavior under Settings > Preference > Metric System. 

Location Tagging
-------
While most users prefer to always have geolocation information tagged to their entry, others may not. So support such users, we have provided this option to never tag geolocation information to your entire. This option can be enabled from Settings > Personalize > Do not add location. 

Note: Changing this option will take effect on a go forward basis and will not remove or add location information from historical posts. 

Do Not Disturb
-------
This option doesn’t affect any functionality but informs our support team to not disturb you or ping you with any survey related questions. This option is turned off by default but can be turned on anytime. 
