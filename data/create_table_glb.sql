DROP TABLE IF EXISTS public.glb;

CREATE TABLE IF NOT EXISTS public.glb(
    year integer NOT NULL,
    jan numeric(4,2),
    feb numeric(4,2),
    mar numeric(4,2),
    apr numeric(4,2),
    may numeric(4,2),
    jun numeric(4,2),
    jul numeric(4,2),
    aug numeric(4,2),
    sep numeric(4,2),
    oct numeric(4,2),
    nov numeric(4,2),
    dec numeric(4,2),
    jtd numeric(4,2),
    dtn numeric(4,2),
    djf numeric(4,2),
    mam numeric(4,2),
    jja numeric(4,2),
    son numeric(4,2),
    CONSTRAINT glb_pkey PRIMARY KEY (year)
)
