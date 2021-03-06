class DropService:

    _DROP_INDEX_ROLE_ID_CAST_INFO = "DROP INDEX IF EXISTS public.role_id_cast_info;"
    _DROP_INDEX_MOVIE_ID_MOVIE_COMPANIES = "DROP INDEX IF EXISTS public.movie_id_movie_companies;"
    _DROP_INDEX_PERSON_ID_AKA_NAME = "DROP INDEX IF EXISTS public.person_id_aka_name;"
    _DROP_INDEX_KEYWORD_ID_MOVIE_KEYWORD = "DROP INDEX IF EXISTS public.keyword_id_movie_keyword;"
    _DROP_INDEX_MOVIE_ID_MOVIE_INFO_IDX = "DROP INDEX IF EXISTS public.movie_id_movie_info_idx;"
    _DROP_INDEX_MOVIE_ID_MOVIE_INFO = "DROP INDEX IF EXISTS public.movie_id_movie_info;"
    _DROP_INDEX_MOVIE_ID_MOVIE_KEYWORD = "DROP INDEX IF EXISTS public.movie_id_movie_keyword;"
    _DROP_INDEX_PERSON_ID_CAST_INFO = "DROP INDEX IF EXISTS public.person_id_cast_info;"
    _DROP_INDEX_MOVIE_ID_CAST_INFO = "DROP INDEX IF EXISTS public.movie_id_cast_info;"
    _DROP_INDEX_PERSON_ROLE_ID_CAST_INFO = "DROP INDEX IF EXISTS public.person_role_id_cast_info;"
    _DROP_INDEX_INFO_TYPE_ID_MOVIE_INFO = "DROP INDEX IF EXISTS public.info_type_id_movie_info;"

    _DROP_CONSTRAINT_NAME_PKEY = "ALTER TABLE IF EXISTS public.name DROP CONSTRAINT IF EXISTS name_pkey;"
    _DROP_CONSTRAINT_TITLE_PKEY = "ALTER TABLE IF EXISTS public.title DROP CONSTRAINT IF EXISTS title_pkey;"
    _DROP_CONSTRAINT_CHAR_NAME_PKEY = "ALTER TABLE IF EXISTS public.char_name DROP CONSTRAINT IF EXISTS char_name_pkey;"
    _DROP_CONSTRAINT_COMPANY_NAME_PKEY = "ALTER TABLE IF EXISTS public.company_name DROP CONSTRAINT IF EXISTS company_name_pkey;"
    _DROP_CONSTRAINT_KIND_TYPE_PKEY = "ALTER TABLE IF EXISTS public.kind_type DROP CONSTRAINT IF EXISTS kind_type_pkey;"
    _DROP_CONSTRAINT_KEYWORD_PKEY = "ALTER TABLE IF EXISTS public.keyword DROP CONSTRAINT IF EXISTS keyword_pkey;"
    _DROP_CONSTRAINT_COMPANY_TYPE_PKEY = "ALTER TABLE IF EXISTS public.company_type DROP CONSTRAINT IF EXISTS company_type_pkey;"
    _DROP_CONSTRAINT_CAST_INFO_PKEY = "ALTER TABLE IF EXISTS public.cast_info DROP CONSTRAINT IF EXISTS cast_info_pkey;"
    _DROP_CONSTRAINT_MOVIE_INFO_PKEY = "ALTER TABLE IF EXISTS public.movie_info DROP CONSTRAINT IF EXISTS movie_info_pkey;"
    _DROP_CONSTRAINT_MOVIE_KEYWORD_PKEY = "ALTER TABLE IF EXISTS public.movie_keyword DROP CONSTRAINT IF EXISTS movie_keyword_pkey;"
    _DROP_CONSTRAINT_MOVIE_COMPANIES_PKEY = "ALTER TABLE IF EXISTS public.movie_companies DROP CONSTRAINT IF EXISTS movie_companies_pkey;"

    DROP_NAMES_ALL_QUERIES = [
        "CAST_INFO_PKEY",
        "MOVIE_INFO_PKEY",
        "PERSON_ID_CAST_INFO",
        "MOVIE_ID_CAST_INFO",
        "PERSON_ROLE_ID_CAST_INFO",
        "ROLE_ID_CAST_INFO",
        "MOVIE_ID_MOVIE_INFO",
        "INFO_TYPE_ID_MOVIE_INFO",
        "MOVIE_KEYWORD_PKEY",
        "NAME_PKEY",
        "MOVIE_COMPANIES_PKEY",
        "TITLE_PKEY"
    ]

    DROP_QUERIES_ALL_QUERIES = [
        _DROP_CONSTRAINT_CAST_INFO_PKEY,
        _DROP_CONSTRAINT_MOVIE_INFO_PKEY,
        _DROP_INDEX_PERSON_ID_CAST_INFO,
        _DROP_INDEX_MOVIE_ID_CAST_INFO,
        _DROP_INDEX_PERSON_ROLE_ID_CAST_INFO,
        _DROP_INDEX_ROLE_ID_CAST_INFO,
        _DROP_INDEX_MOVIE_ID_MOVIE_INFO,
        _DROP_INDEX_INFO_TYPE_ID_MOVIE_INFO,
        _DROP_CONSTRAINT_MOVIE_KEYWORD_PKEY,
        _DROP_CONSTRAINT_NAME_PKEY,
        _DROP_CONSTRAINT_MOVIE_COMPANIES_PKEY,
        _DROP_CONSTRAINT_TITLE_PKEY
    ]

    DROP_NAMES_Q22C = [
        "KEYWORD_ID_MOVIE_KEYWORD",
        "TITLE_PKEY",
        "MOVIE_ID_MOVIE_COMPANIES",
        "MOVIE_ID_MOVIE_INFO_IDX",
        "COMPANY_NAME_PKEY",
        "MOVIE_ID_MOVIE_INFO",
        "KIND_TYPE_PKEY",
        "MOVIE_ID_MOVIE_KEYWORD",
        "KEYWORD_PKEY",
        "COMPANY_TYPE_PKEY"
    ]

    DROP_QUERIES_Q22C = [
        _DROP_INDEX_KEYWORD_ID_MOVIE_KEYWORD,
        _DROP_CONSTRAINT_TITLE_PKEY,
        _DROP_INDEX_MOVIE_ID_MOVIE_COMPANIES,
        _DROP_INDEX_MOVIE_ID_MOVIE_INFO_IDX,
        _DROP_CONSTRAINT_COMPANY_NAME_PKEY,
        _DROP_INDEX_MOVIE_ID_MOVIE_INFO,
        _DROP_CONSTRAINT_KIND_TYPE_PKEY,
        _DROP_INDEX_MOVIE_ID_MOVIE_KEYWORD,
        _DROP_CONSTRAINT_KEYWORD_PKEY,
        _DROP_CONSTRAINT_COMPANY_TYPE_PKEY
    ]

    DROP_NAMES_Q9A = [
        "ROLE_ID_CAST_INFO",
        "NAME_PKEY",
        "TITLE_PKEY",
        "CHAR_NAME_PKEY",
        "MOVIE_ID_MOVIE_COMPANIES",
        "COMPANY_NAME_PKEY",
        "PERSON_ID_AKA_NAME"
    ]

    DROP_QUERIES_Q9A = [
        _DROP_INDEX_ROLE_ID_CAST_INFO,
        _DROP_CONSTRAINT_NAME_PKEY,
        _DROP_CONSTRAINT_TITLE_PKEY,
        _DROP_CONSTRAINT_CHAR_NAME_PKEY,
        _DROP_INDEX_MOVIE_ID_MOVIE_COMPANIES,
        _DROP_CONSTRAINT_COMPANY_NAME_PKEY,
        _DROP_INDEX_PERSON_ID_AKA_NAME
    ]

    assert(len(DROP_NAMES_Q9A) == len(DROP_QUERIES_Q9A))
    assert(len(DROP_NAMES_Q22C) == len(DROP_QUERIES_Q22C))
    assert(len(DROP_NAMES_ALL_QUERIES) == len(DROP_QUERIES_ALL_QUERIES))
