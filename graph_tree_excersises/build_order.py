"""
Build Order
You are given a list of projects and a list of dependencies
(which is a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built.
If there is no valid build order, return an error.
E.g.
Projects: a,b,c,d,e,f
dependencies: ad(d from a), fb, bd, fa, dc
Output: e, f, a, b, d, c
"""
from typing import List, Tuple


def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph


def findBuildOrder(projects, dependencies):
    dependency_map = createGraph(projects, dependencies)
    build_order = []
    project_set = set(project)
    set_len = len(project_set)
    while len(build_order) < len(project):
        dependent_set = set()
        for d_list in dependency_map.values():
            dependent_set = dependent_set.union(d_list)

        independent_set = project_set.difference(dependent_set)

        for el in independent_set:
            if el in dependency_map.keys():
                del dependency_map[el]
                build_order.append(el)

        project_set.difference_update(independent_set)

        if set_len == len(project_set):
            build_order = []
            break
        set_len = len(project_set)
    return build_order


def test_build_dep():
    # project = ['a', 'b', 'c', 'd', 'e', 'f']
    # dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]
    # { a: f, b: f, c: d, d:[a,b], e:[], f:[]} -- {a:d, b:d, c:[], d:c, e:[], f:[a,b]}
    # { a: f, b: f, c: d, d:[a,b]} -- {a:d, b:d, d:c, f:[a,b]}
    # a b c d
    # { a: f, b: f, c: d, d:[a,b]} -- {a:d, b:d, d:c, f:[a,b]}
    # f not in set -> delete key f
    # a b c d
    # { a: f, b: f, c: d, d:[a,b]} -- {a:d, b:d, d:c}
    #

    dependencies = [('a','d'), ('b','f'), ('b','d'), ('f','a'), ('d','c')]
    project = ['a', 'b', 'c', 'd', 'e', 'f']

    print(findBuildOrder(project,dependencies))

    # project_set = set(project)
    # map_dependency = {key: [] for key in project}
    # for dependency in dependencies:
    #     map_dependency[dependency[0]].append(dependency[1])
    #
    # build_order = []
    # project_set = set(project)
    # set_len = len(project_set)
    # while len(build_order) < len(project):
    #     dependent_set = set()
    #     for ll in map_dependency.values():
    #         dependent_set = dependent_set.union(ll)
    #     independent_set = project_set.difference(dependent_set)
    #     for el in independent_set:
    #         if el in map_dependency.keys():
    #             del map_dependency[el]
    #             build_order.append(el)
    #
    #     project_set.difference_update(independent_set)
    #     if set_len == len(project_set):
    #         print("error")
    #         break
    #     set_len = len(project_set)
    #
    # print(build_order)
    #
    #
    # print(map_dependency.values())
