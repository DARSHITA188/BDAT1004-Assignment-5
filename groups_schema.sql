-- # -*- coding: utf-8 -*-

-- Created on Mon Jun 17 11:35:50 2019

-- @author: 17057

-- Group table

create table grp (
        ID                  text primary key,
        Name                text,
        Course_ID           text
        );

-- Course table

create table course (
        Course_ID           text primary key,
        Course_Name         text
        );
        
        