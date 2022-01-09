from tqdm import tqdm

import executor_utils


class RepairService:
    _ANALYZE = "analyze;"
    _CREATE_INDEX_MOVIE_ID_CAST_INFO = "CREATE INDEX IF NOT EXISTS movie_id_cast_info ON public.cast_info USING btree (movie_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_ROLE_ID_CAST_INFO = "CREATE INDEX IF NOT EXISTS role_id_cast_info ON public.cast_info USING btree (role_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_MOVIE_ID_MOVIE_COMPANIES = "CREATE INDEX IF NOT EXISTS movie_id_movie_companies ON public.movie_companies USING btree (movie_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_PERSON_ID_AKA_NAME = "CREATE INDEX IF NOT EXISTS person_id_aka_name ON public.aka_name USING btree (person_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_KEYWORD_ID_MOVIE_KEYWORD = "CREATE INDEX IF NOT EXISTS keyword_id_movie_keyword ON public.movie_keyword USING btree (keyword_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_MOVIE_ID_MOVIE_INFO_IDX = "CREATE INDEX IF NOT EXISTS movie_id_movie_info_idx ON public.movie_info_idx USING btree (movie_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_MOVIE_ID_MOVIE_INFO = "CREATE INDEX IF NOT EXISTS movie_id_movie_info ON public.movie_info USING btree (movie_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_MOVIE_ID_MOVIE_KEYWORD = "CREATE INDEX IF NOT EXISTS movie_id_movie_keyword ON public.movie_keyword USING btree (movie_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_PERSON_ID_CAST_INFO = "CREATE INDEX IF NOT EXISTS person_id_cast_info ON public.cast_info USING btree (person_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_PERSON_ROLE_ID_CAST_INFO = "CREATE INDEX IF NOT EXISTS person_role_id_cast_info ON public.cast_info USING btree (person_role_id ASC NULLS LAST) TABLESPACE pg_default;"
    _CREATE_INDEX_INFO_TYPE_ID_MOVIE_INFO = "CREATE INDEX IF NOT EXISTS info_type_id_movie_info ON public.movie_info USING btree (info_type_id ASC NULLS LAST) TABLESPACE pg_default;"

    _ADD_CONSTRAINT_TITLE_PKEY = "ALTER TABLE IF EXISTS public.title ADD CONSTRAINT title_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_ROLE_TYPE_PKEY = "ALTER TABLE IF EXISTS public.role_type ADD CONSTRAINT role_type_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_CHAR_NAME_PKEY = "ALTER TABLE IF EXISTS public.char_name ADD CONSTRAINT char_name_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_COMPANY_TYPE_PKEY = "ALTER TABLE IF EXISTS public.company_type ADD CONSTRAINT company_type_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_COMPANY_NAME_PKEY = "ALTER TABLE IF EXISTS public.company_name ADD CONSTRAINT company_name_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_NAME_PKEY = "ALTER TABLE IF EXISTS public.name ADD CONSTRAINT name_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_KIND_TYPE_PKEY = "ALTER TABLE IF EXISTS public.kind_type ADD CONSTRAINT kind_type_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_KEYWORD_PKEY = "ALTER TABLE IF EXISTS public.keyword ADD CONSTRAINT keyword_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_CAST_INFO_PKEY = "ALTER TABLE IF EXISTS public.cast_info ADD CONSTRAINT cast_info_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_MOVIE_INFO_PKEY = "ALTER TABLE IF EXISTS public.movie_info ADD CONSTRAINT movie_info_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_MOVIE_KEYWORD_PKEY = "ALTER TABLE IF EXISTS public.movie_keyword ADD CONSTRAINT movie_keyword_pkey PRIMARY KEY (id);"
    _ADD_CONSTRAINT_MOVIE_COMPANIES_PKEY = "ALTER TABLE IF EXISTS public.movie_companies ADD CONSTRAINT movie_companies_pkey PRIMARY KEY (id);"

    INDICES_ALL_QUERIES = [
        _ADD_CONSTRAINT_CAST_INFO_PKEY,
        _ADD_CONSTRAINT_MOVIE_INFO_PKEY,
        _CREATE_INDEX_PERSON_ID_CAST_INFO,
        _CREATE_INDEX_MOVIE_ID_CAST_INFO,
        _CREATE_INDEX_PERSON_ROLE_ID_CAST_INFO,
        _CREATE_INDEX_ROLE_ID_CAST_INFO,
        _CREATE_INDEX_MOVIE_ID_MOVIE_INFO,
        _CREATE_INDEX_INFO_TYPE_ID_MOVIE_INFO,
        _ADD_CONSTRAINT_MOVIE_KEYWORD_PKEY,
        _ADD_CONSTRAINT_NAME_PKEY,
        _ADD_CONSTRAINT_MOVIE_COMPANIES_PKEY,
        _ADD_CONSTRAINT_TITLE_PKEY,
        _ANALYZE
    ]

    INDICES_Q22C = [
        _CREATE_INDEX_KEYWORD_ID_MOVIE_KEYWORD,
        _ADD_CONSTRAINT_TITLE_PKEY,
        _CREATE_INDEX_MOVIE_ID_MOVIE_COMPANIES,
        _CREATE_INDEX_MOVIE_ID_MOVIE_INFO_IDX,
        _ADD_CONSTRAINT_COMPANY_NAME_PKEY,
        _CREATE_INDEX_MOVIE_ID_MOVIE_INFO,
        _ADD_CONSTRAINT_KIND_TYPE_PKEY,
        _CREATE_INDEX_MOVIE_ID_MOVIE_KEYWORD,
        _ADD_CONSTRAINT_KEYWORD_PKEY,
        _ADD_CONSTRAINT_COMPANY_TYPE_PKEY,
        _ANALYZE
    ]

    INDICES_Q10A = [
        _CREATE_INDEX_ROLE_ID_CAST_INFO,
        _ADD_CONSTRAINT_CHAR_NAME_PKEY,
        _ADD_CONSTRAINT_TITLE_PKEY,
        _ADD_CONSTRAINT_COMPANY_TYPE_PKEY,
        _CREATE_INDEX_MOVIE_ID_CAST_INFO,
        _CREATE_INDEX_MOVIE_ID_MOVIE_COMPANIES,
        _ADD_CONSTRAINT_COMPANY_NAME_PKEY,
        _ANALYZE
    ]

    INDICES_Q9A = [
        _CREATE_INDEX_ROLE_ID_CAST_INFO,
        _ADD_CONSTRAINT_NAME_PKEY,
        _ADD_CONSTRAINT_TITLE_PKEY,
        _ADD_CONSTRAINT_CHAR_NAME_PKEY,
        _CREATE_INDEX_MOVIE_ID_MOVIE_COMPANIES,
        _ADD_CONSTRAINT_COMPANY_NAME_PKEY,
        _CREATE_INDEX_PERSON_ID_AKA_NAME,
        _ANALYZE
    ]

    def repair_indices_all_queries(self):
        self.repair_indices(self.INDICES_ALL_QUERIES, "all queries")

    def repair_indices_q9a(self):
        self.repair_indices(self.INDICES_Q9A, "q9a")

    def repair_indices_q22c(self):
        self.repair_indices(self.INDICES_Q22C, "q22c")

    def repair_indices(self, indices, name):
        print(f"Repairing indices for query {name}")

        for i in tqdm(range(len(indices))):
            query = indices[i]
            executor_utils.run_query(query)

        print("Finished repair")
        