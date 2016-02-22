#!/usr/bin/env python

import unittest
import sys

class ImportTest(unittest.TestCase):
    def testImportAnnotation(self):
        success = False
        try:
            from cutlass import Annotation
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Annotation is None)

    def testImportIHMPSession(self):
        success = False
        try:
            from cutlass import iHMPSession
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(iHMPSession is None)

    def testImportProject(self):
        success = False

        try:
            from cutlass import Project
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Project is None)

    def testImportProteome(self):
        success = False

        try:
            from cutlass import Proteome
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Proteome is None)

    def testImportStudy(self):
        success = False

        try:
            from cutlass import Study
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Study is None)

    def testImportSubject(self):
        success = False

        try:
            from cutlass import Subject
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Subject is None)

    def testImportVisit(self):
        success = False

        try:
            from cutlass import Visit
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Visit is None)

    def testImport16SDnaPrep(self):
        success = False

        try:
            from cutlass import SixteenSDnaPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSDnaPrep is None)

    def testImportWgsAssembledSeqSet(self):
        success = False

        try:
            from cutlass import WgsAssembledSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(WgsAssembledSeqSet is None)

    def testImportWgsDnaPrep(self):
        success = False

        try:
            from cutlass import WgsDnaPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(WgsDnaPrep is None)

    def testImport16SRawSeqSet(self):
        success = False

        try:
            from cutlass import SixteenSRawSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSRawSeqSet is None)

    def testImportWgsRawSeqSet(self):
        success = False

        try:
            from cutlass import WgsRawSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(WgsRawSeqSet is None)

    def testImport16STrimmedSeqSet(self):
        success = False

        try:
            from cutlass import SixteenSTrimmedSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSTrimmedSeqSet is None)

    def testImportHostAssayPrep(self):
        success = False

        try:
            from cutlass import HostAssayPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(HostAssayPrep is None)

    def testImportMicrobiomeAssayPrep(self):
        success = False

        try:
            from cutlass import MicrobiomeAssayPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MicrobiomeAssayPrep is None)

    def testImportMIMS(self):
        success = False

        try:
            from cutlass import MIMS
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MIMS is None)

    def testImportMIMARKS(self):
        success = False

        try:
            from cutlass import MIMARKS
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MIMARKS is None)

    def testImportMIXS(self):
        success = False

        try:
            from cutlass import MIXS
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MIXS is None)

    def testImportAspera(self):
        success = False

        try:
            from cutlass import aspera
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(aspera is None)

if __name__ == '__main__':
    unittest.main()
