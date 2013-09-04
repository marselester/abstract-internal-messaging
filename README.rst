==================================
Abstract Internal Messaging System
==================================

This is an interview test task.

Allow sending of messages between individual users, identified by the unique
key of their record in the system. Messages are in markdown format, and
auto-complete of recipients would be a bonus.

Allow a user to view their inbox, read messages, (automatically) mark messages
as read, and delete messages.

Allow sending a broadcast message to all users. Keep in mind that there could
be millions of users.

Allow sending a message to a group of users. Groups can be large (over 100,000
users) and are stored by having each user record list all the groups it’s a
member of. Group membership varies over time and a message should be received
only by the users who were members of the destination group at the time the
message was sent.
