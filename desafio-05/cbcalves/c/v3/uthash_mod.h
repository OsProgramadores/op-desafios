/*
ATTENTION !!!!!!

THIS IS NOT THE ORIGINAL UTHASH TABLE, DOWNLOAD ORIGINAL FROM THE SITE
http://troydhanson.github.com/uthash/

THIS IS A MODIFIED VERSION TO BE USED IN:
https://github.com/OsProgramadores/op-desafios/tree/master/desafio-05

ATENÇÃO !!!!!!

ESTE NÃO É O UTHASH ORIGINAL, FAÇA O DOWNLOAD DO ORIGINAL DO SITE
http://troydhanson.github.com/uthash/

ESTA VERSÃO FOI MODIFICADA PARA SER USADA EM:
https://github.com/OsProgramadores/op-desafios/tree/master/desafio-05


Copyright (c) 2003-2018, Troy D. Hanson     http://troydhanson.github.com/uthash/
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#ifndef UTHASH_H
#define UTHASH_H

#define UTHASH_VERSION 2.1.x

#include <string.h> /* memcmp, memset, strlen */
#include <stddef.h> /* ptrdiff_t */
#include <stdlib.h> /* exit */
#include <stdint.h>

/* These macros use decltype or the earlier __typeof GNU extension.
   As decltype is only available in newer compilers (VS2010 or gcc 4.3+
   when compiling c++ source) this code uses whatever method is needed
   or, for VS2008 where neither is available, uses casting workarounds. */
#define DECLTYPE(x) (__typeof(x))
#define DECLTYPE_ASSIGN(dst, src) (dst) = (__typeof(dst))(src);

/* initial number of buckets */
#define HASH_INITIAL_NUM_BUCKETS 2048U    /* initial number of buckets        */
#define HASH_INITIAL_NUM_BUCKETS_LOG2 11U /* lg2 of initial number of buckets */
#define HASH_BKT_CAPACITY_THRESH 10U      /* expand when bucket count reaches */

/* calculate the element whose hash handle address is hhp */
#define ELMT_FROM_HH(tbl, hhp) ((void *)(((char *)(hhp)) - ((tbl)->hho)))
/* calculate the hash handle from element address elp */
#define HH_FROM_ELMT(tbl, elp) ((UT_hash_handle *)(void *)(((char *)(elp)) + ((tbl)->hho)))

#define HASH_VALUE(keyptr, keylen, hashv) HASH_FCN(keyptr, keylen, hashv)

#define HASH_TO_BKT(hashv, num_bkts, bkt) bkt = ((hashv) & ((num_bkts)-1U));

/* iterate over items in a known bucket to find desired item */
#define HASH_FIND_IN_BKT(tbl, hh, head, keylen_in, hashval, out)                   \
    {                                                                              \
        if ((head).hh_head != NULL) {                                              \
            DECLTYPE_ASSIGN(out, ELMT_FROM_HH(tbl, (head).hh_head));               \
        } else {                                                                   \
            (out) = NULL;                                                          \
        }                                                                          \
        while ((out) != NULL) {                                                    \
            if ((out)->hh.hashv == (hashval) && (out)->hh.keylen == (keylen_in)) { \
                break;                                                             \
            }                                                                      \
            if ((out)->hh.hh_next != NULL) {                                       \
                DECLTYPE_ASSIGN(out, ELMT_FROM_HH(tbl, (out)->hh.hh_next));        \
            } else {                                                               \
                (out) = NULL;                                                      \
                break;                                                             \
            }                                                                      \
        }                                                                          \
    }

/* add an item to a bucket  */
#define HASH_ADD_TO_BKT(head, hh, addhh)           \
    {                                              \
        (&(head))->count++;                        \
        (addhh)->hh_next = (&(head))->hh_head;     \
        (addhh)->hh_prev = NULL;                   \
        if ((&(head))->hh_head != NULL) {          \
            (&(head))->hh_head->hh_prev = (addhh); \
        }                                          \
        (&(head))->hh_head = (addhh);              \
    }

#define HASH_FIND_BYHASHVALUE(hh, head, keyptr, keylen, hashval, out)                                 \
    {                                                                                                 \
        unsigned _hf_bkt;                                                                             \
        HASH_TO_BKT(hashval, (head)->hh.tbl->num_buckets, _hf_bkt);                                   \
        HASH_FIND_IN_BKT((head)->hh.tbl, hh, (head)->hh.tbl->buckets[_hf_bkt], keylen, hashval, out); \
    }

#define HASH_MAKE_TABLE(hh, head)                                           \
    {                                                                       \
        (head)->hh.tbl = (UT_hash_table *)calloc(1, sizeof(UT_hash_table)); \
        (head)->hh.tbl->tail = &((head)->hh);                               \
        (head)->hh.tbl->num_buckets = HASH_INITIAL_NUM_BUCKETS;             \
        (head)->hh.tbl->log2_num_buckets = HASH_INITIAL_NUM_BUCKETS_LOG2;   \
        (head)->hh.tbl->hho = (char *)(&(head)->hh) - (char *)(head);       \
        (head)->hh.tbl->buckets = (UT_hash_bucket *)calloc(                 \
            HASH_INITIAL_NUM_BUCKETS, sizeof(struct UT_hash_bucket));       \
    }

#define HASH_ADD_BYHASHVALUE(hh, head, hashval, add)                         \
    {                                                                        \
        unsigned _ha_bkt;                                                    \
        (add)->hh.tbl = (head)->hh.tbl;                                      \
        (add)->hh.prev = ELMT_FROM_HH((head)->hh.tbl, (head)->hh.tbl->tail); \
        (add)->hh.next = NULL;                                               \
        (head)->hh.tbl->tail->next = (add);                                  \
        (head)->hh.tbl->tail = &((add)->hh);                                 \
        (head)->hh.tbl->num_items++;                                         \
        HASH_TO_BKT(hashval, (head)->hh.tbl->num_buckets, _ha_bkt);          \
        HASH_ADD_TO_BKT((head)->hh.tbl->buckets[_ha_bkt], hh, &(add)->hh);   \
    }

#define HASH_FCN HASH_JEN

#define HASH_JEN_MIX(a, b, c) \
    {                         \
        a -= b;               \
        a -= c;               \
        a ^= (c >> 13);       \
        b -= c;               \
        b -= a;               \
        b ^= (a << 8);        \
        c -= a;               \
        c -= b;               \
        c ^= (b >> 13);       \
        a -= b;               \
        a -= c;               \
        a ^= (c >> 12);       \
        b -= c;               \
        b -= a;               \
        b ^= (a << 16);       \
        c -= a;               \
        c -= b;               \
        c ^= (b >> 5);        \
        a -= b;               \
        a -= c;               \
        a ^= (c >> 3);        \
        b -= c;               \
        b -= a;               \
        b ^= (a << 10);       \
        c -= a;               \
        c -= b;               \
        c ^= (b >> 15);       \
    }

#define HASH_JEN(key, keylen, hashv)                                                                                             \
    {                                                                                                                            \
        unsigned _hj_i, _hj_j, _hj_k;                                                                                            \
        unsigned const char *_hj_key = (unsigned const char *)(key);                                                             \
        hashv = 0xfeedbeefu;                                                                                                     \
        _hj_i = _hj_j = 0x9e3779b9u;                                                                                             \
        _hj_k = (unsigned)(keylen);                                                                                              \
        while (_hj_k >= 12U) {                                                                                                   \
            _hj_i += (_hj_key[0] + ((unsigned)_hj_key[1] << 8) + ((unsigned)_hj_key[2] << 16) + ((unsigned)_hj_key[3] << 24));   \
            _hj_j += (_hj_key[4] + ((unsigned)_hj_key[5] << 8) + ((unsigned)_hj_key[6] << 16) + ((unsigned)_hj_key[7] << 24));   \
            hashv += (_hj_key[8] + ((unsigned)_hj_key[9] << 8) + ((unsigned)_hj_key[10] << 16) + ((unsigned)_hj_key[11] << 24)); \
                                                                                                                                 \
            HASH_JEN_MIX(_hj_i, _hj_j, hashv);                                                                                   \
                                                                                                                                 \
            _hj_key += 12;                                                                                                       \
            _hj_k -= 12U;                                                                                                        \
        }                                                                                                                        \
        hashv += (unsigned)(keylen);                                                                                             \
        switch (_hj_k) {                                                                                                         \
        case 11:                                                                                                                 \
            hashv += ((unsigned)_hj_key[10] << 24); /* FALLTHROUGH */                                                            \
        case 10:                                                                                                                 \
            hashv += ((unsigned)_hj_key[9] << 16); /* FALLTHROUGH */                                                             \
        case 9:                                                                                                                  \
            hashv += ((unsigned)_hj_key[8] << 8); /* FALLTHROUGH */                                                              \
        case 8:                                                                                                                  \
            _hj_j += ((unsigned)_hj_key[7] << 24); /* FALLTHROUGH */                                                             \
        case 7:                                                                                                                  \
            _hj_j += ((unsigned)_hj_key[6] << 16); /* FALLTHROUGH */                                                             \
        case 6:                                                                                                                  \
            _hj_j += ((unsigned)_hj_key[5] << 8); /* FALLTHROUGH */                                                              \
        case 5:                                                                                                                  \
            _hj_j += _hj_key[4]; /* FALLTHROUGH */                                                                               \
        case 4:                                                                                                                  \
            _hj_i += ((unsigned)_hj_key[3] << 24); /* FALLTHROUGH */                                                             \
        case 3:                                                                                                                  \
            _hj_i += ((unsigned)_hj_key[2] << 16); /* FALLTHROUGH */                                                             \
        case 2:                                                                                                                  \
            _hj_i += ((unsigned)_hj_key[1] << 8); /* FALLTHROUGH */                                                              \
        case 1:                                                                                                                  \
            _hj_i += _hj_key[0];                                                                                                 \
        }                                                                                                                        \
        HASH_JEN_MIX(_hj_i, _hj_j, hashv);                                                                                       \
    }

typedef struct UT_hash_bucket {
    struct UT_hash_handle *hh_head;
    unsigned count;
} UT_hash_bucket;

typedef struct UT_hash_table {
    UT_hash_bucket *buckets;
    unsigned num_buckets, log2_num_buckets;
    unsigned num_items;
    struct UT_hash_handle *tail; /* tail hh in app order, for fast append    */
    ptrdiff_t hho;               /* hash handle offset (byte pos of hash handle in element */
} UT_hash_table;

typedef struct UT_hash_handle {
    struct UT_hash_table *tbl;
    void *prev;                     /* prev element in app order      */
    void *next;                     /* next element in app order      */
    struct UT_hash_handle *hh_prev; /* previous hh in bucket order    */
    struct UT_hash_handle *hh_next; /* next hh in bucket order        */
    const char *key;                /* ptr to enclosing struct's key  */
    unsigned char keylen;           /* enclosing struct's key len     */
    unsigned hashv;                 /* result of hash-fcn(key)        */
} UT_hash_handle;

#endif /* UTHASH_H */
