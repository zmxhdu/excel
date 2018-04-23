-- Create table
create table TRISK_USER
(
  user_id       VARCHAR2(50),
  user_password VARCHAR2(100),
  user_name     VARCHAR2(100)
);
-- Add comments to the table 
comment on table TRISK_USER
  is '用户信息表';
-- Add comments to the columns 
comment on column TRISK_USER.user_id
  is '用户账户';
comment on column TRISK_USER.user_password
  is '用户密码';
comment on column TRISK_USER.user_name
  is '用户名';
-- Create table
create table TRISK_PROJECT
(
  project_id      NUMBER,
  project_name    VARCHAR2(50),
  project_remarks VARCHAR2(4000)
) ;
-- Add comments to the table 
comment on table TRISK_PROJECT
  is '项目表(客户表)';
-- Add comments to the columns 
comment on column TRISK_PROJECT.project_id
  is '项目(客户)ID';
comment on column TRISK_PROJECT.project_name
  is '名称';
comment on column TRISK_PROJECT.project_remarks
  is '备注';
-- Create table
create table TRISK_TASK
(
  task_id     VARCHAR2(50),
  task_type   VARCHAR2(10),
  task_detail VARCHAR2(4000)
) ;
-- Add comments to the table 
comment on table TRISK_TASK
  is 'OA信息表（外部导入）';
-- Add comments to the columns 
comment on column TRISK_TASK.task_id
  is 'OA号';
comment on column TRISK_TASK.task_type
  is 'OA类型';
comment on column TRISK_TASK.task_detail
  is 'OA明细';
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
  is '工作表';
-- Add comments to the columns 
comment on column TRISK_WORK.work_id
  is '工作ID自动生成';
comment on column TRISK_WORK.task_id
  is '任务ID OA号';
comment on column TRISK_PROJECT.project_id
  is '项目(客户)ID';
comment on column TRISK_WORK.transactor_id
  is '经办人ID';
comment on column TRISK_WORK.dev_id
  is '开发人员ID';
comment on column TRISK_WORK.work_start
  is '任务开始时间';
comment on column TRISK_WORK.development
  is '开发进度';
comment on column TRISK_WORK.work_status
  is '开发状态 0：未开始，1：正在进行，2 ：提交测试，3：完成，-1：暂停';
comment on column TRISK_WORK.work_text
  is '备注';
comment on column TRISK_WORK.work_end
  is '任务结束时间';
