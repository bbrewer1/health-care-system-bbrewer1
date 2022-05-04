# Health Care Sytem API

## Description

The purpose of this API is to provide the working backend of a healthcare system. There are roles for patients, doctors, nurses, admins, etc. Furthermore, users info such as billing info, their measurements, medical record history, what medical devices they have access to, etc. can all be updated by doctors, nurses, and admins. 

## Schemas

The API follows the schema below
![schema](https://github.com/bbrewer1/health-care-system-bbrewer1/blob/master/schema_diagram.jpg)

## Chat

There is also a chat module so that doctors can be connected directly to patients. It's a redumentary chatroom, so it's on the users to come up with a way to securely generate and share the name of a chatroom

## Threading

The API implements basic threading so that cocurrent requests do not crash the system or get lost

## Usage

The API is configured to run on an EC2 instance or locally on host (easier for testing). To run on an EC2 instance, contact `bbrewer1@bu.edu` for details.
