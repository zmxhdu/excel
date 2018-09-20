-- Create table
create table TRISK_USER
(
  id            VARCHAR2(50),
  user_id       VARCHAR2(50),
  user_password VARCHAR2(100),
  user_name     VARCHAR2(100),
  user_role     VARCHAR2(50)
);
-- Add comments to the table
comment on table TRISK_USER
  is '�û���Ϣ��';
-- Add comments to the columns
comment on column TRISK_USER.id
  is 'ID�Զ�����';
comment on column TRISK_USER.user_id
  is '�û��˻�';
comment on column TRISK_USER.user_password
  is '�û�����';
comment on column TRISK_USER.user_name
  is '�û���';
comment on column TRISK_USER.user_role
is '�û���ɫ';

alter table TRISK_USER add constraint pk_id primary key(id);

create sequence S_TRISK_USER
increment by 1
start with 1
nomaxvalue
nominvalue
nocache;

create or replace trigger INSERT_TRISK_USER before insert on TRISK_USER
referencing old as old new as new
for each row
begin
    select S_TRISK_USER.nextval into :NEW.ID from dual;
end;
/
-- Create table
create table TRISK_PROJECT
(
  project_id      NUMBER,
  project_name    VARCHAR2(50),
  project_remarks VARCHAR2(4000)
) ;
-- Add comments to the table 
comment on table TRISK_PROJECT
  is '��Ŀ��(�ͻ���)';
-- Add comments to the columns 
comment on column TRISK_PROJECT.project_id
  is '��Ŀ(�ͻ�)ID';
comment on column TRISK_PROJECT.project_name
  is '����';
comment on column TRISK_PROJECT.project_remarks
  is '��ע';
-- Create table
create table TRISK_TASK
(
  task_id     VARCHAR2(50),
  task_type   VARCHAR2(10),
  task_detail VARCHAR2(4000)
) ;
-- Add comments to the table 
comment on table TRISK_TASK
  is 'OA��Ϣ���ⲿ���룩';
-- Add comments to the columns 
comment on column TRISK_TASK.task_id
  is 'OA��';
comment on column TRISK_TASK.task_type
  is 'OA����';
comment on column TRISK_TASK.task_detail
  is 'OA��ϸ';
-- Create table
create table TRISK_WORK
(
  work_id       NUMBER,
  task_id       VARCHAR2(50),
  project_id    VARCHAR2(50),
  transactor_id VARCHAR2(50),
  dev_id        VARCHAR2(50),
  work_start    DATE,
  development   NUMBER,
  work_status   NUMBER,
  work_text     VARCHAR2(4000),
  work_end      DATE
);
-- Add comments to the table 
comment on table TRISK_WORK
  is '������';
-- Add comments to the columns 
comment on column TRISK_WORK.work_id
  is '����ID�Զ�����';
comment on column TRISK_WORK.task_id
  is '����ID OA��';
comment on column TRISK_PROJECT.project_id
  is '��Ŀ(�ͻ�)ID';
comment on column TRISK_WORK.transactor_id
  is '������ID';
comment on column TRISK_WORK.dev_id
  is '������ԱID';
comment on column TRISK_WORK.work_start
  is '����ʼʱ��';
comment on column TRISK_WORK.development
  is '��������';
comment on column TRISK_WORK.work_status
  is '����״̬ 0��δ��ʼ��1�����ڽ��У�2 ���ύ���ԣ�3����ɣ�-1����ͣ';
comment on column TRISK_WORK.work_text
  is '��ע';
comment on column TRISK_WORK.work_end
  is '�������ʱ��';
  
  
create sequence S_TRISK_WORK
increment by 1
start with 1
nomaxvalue
nominvalue
nocache;

create or replace trigger INSERT_TRISK_WORK before insert on TRISK_WORK
referencing old as old new as new
for each row
begin
    select S_TRISK_WORK.nextval into :NEW.WORK_ID from dual;
end;
/