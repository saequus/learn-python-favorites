# ============================================================================
# ================= Remove Empty Lists and Dicts From JSON ===================
# ============================================================================

import json


class RemoveEmptyListsDictsFromJSON:
    def delete_empty(self, obj):
        new_obj = self._check_and_remove(obj)
        new_obj = self._remove_null_values(new_obj)
        return new_obj

    def _check_and_remove(self, obj):
        if isinstance(obj, list):
            li = [self._check_and_remove(_) for _ in obj if _ != {} and _ != []
                  and _ is not None]
            return li if li != [] else None
        if isinstance(obj, dict):
            obj = {k: self._check_and_remove(v) for k, v in obj.items() if v}
            return obj if obj != {} else None
        return obj

    def _remove_null_values(self, obj):
        if isinstance(obj, str):
            obj = json.loads(obj)
        if isinstance(obj, list):
            return [self._check_and_remove(_) for _ in obj if _ is not None
                    and _ is not None]
        if isinstance(obj, dict):
            obj = {k: self._check_and_remove(v) for k, v in obj.items() if v}
            return {k: self._check_and_remove(v) for k, v in obj.items() if v}


# ============================== Code Driver =================================


test1 = {
    'part-one': [],
    'internal': [[], ['a']],
    'before-last': {},
    'last': [{3: []}, {4: [{}, 'fa', {}]}]
}
test2 = {1: [], 2: []}
test3 = {
    'first': [],
    'second': [[], {}, [[], 'a', 'b']],
    'third': ['one_persons_table', 'two_persons_table'],
    'menu': [[], ['basic', '', [], 'private', {}, {}]],
    'ingredients': {
        'places': [],
        'variants': {
            '3': '1',
            'objects': [],
            'spaces': {}
        }
    }
}

remover = RemoveEmptyListsDictsFromJSON()

test1_json = json.dumps(test1)
print(remover.delete_empty(test1_json))

test2_json = json.dumps(test2)
print(remover.delete_empty(test2_json))

test3_json = json.dumps(test3)
print(remover.delete_empty(test3_json))

