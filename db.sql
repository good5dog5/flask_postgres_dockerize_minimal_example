--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: jordan
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO jordan;

--
-- Name: user_info; Type: TABLE; Schema: public; Owner: jordan
--

CREATE TABLE public.user_info (
    id integer NOT NULL,
    first_name character varying(20),
    last_name character varying(20),
    email character varying(40),
    mobile character varying(40),
    job_title character varying(20)
);


ALTER TABLE public.user_info OWNER TO jordan;

--
-- Name: user_info_id_seq; Type: SEQUENCE; Schema: public; Owner: jordan
--

CREATE SEQUENCE public.user_info_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_info_id_seq OWNER TO jordan;

--
-- Name: user_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jordan
--

ALTER SEQUENCE public.user_info_id_seq OWNED BY public.user_info.id;


--
-- Name: user_info id; Type: DEFAULT; Schema: public; Owner: jordan
--

ALTER TABLE ONLY public.user_info ALTER COLUMN id SET DEFAULT nextval('public.user_info_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: jordan
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: user_info; Type: TABLE DATA; Schema: public; Owner: jordan
--

COPY public.user_info (id, first_name, last_name, email, mobile, job_title) FROM stdin;
1	jordan	huang	jordan.huang@gapp.nthu.edu.tw	0960135798	SRE
2	a	b	good@kind.com	09213432423	SRE
3	a	b	c	d	e
4	jordan	b	dsfsf@gapp.com	dfsd	fsfsdfs
\.


--
-- Name: user_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jordan
--

SELECT pg_catalog.setval('public.user_info_id_seq', 4, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: jordan
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: user_info user_info_pkey; Type: CONSTRAINT; Schema: public; Owner: jordan
--

ALTER TABLE ONLY public.user_info
    ADD CONSTRAINT user_info_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

