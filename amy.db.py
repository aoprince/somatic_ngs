
import csv
import sqlalchemy

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Float, insert

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session

from sqlalchemy.orm import Mapped

from sqlalchemy.orm import relationship

import pandas as pd





Base = declarative_base()



# Declare models

class Sample(Base):

    __tablename__ = "samples"



    sample_id = Column(String, primary_key=True)

    sample_run = relationship(

        'Sample_run', back_populates="sample", cascade="all, delete-orphan"

    )



    def __repr__(self):

        return f"({self.sample_id})"

    



class Sample_run(Base):

    __tablename__ = "sample_run"



    sample_run_id = Column(Integer, primary_key=True)

    sample_id = Column(Integer, ForeignKey("samples.sample_id"))

    run_id = Column(Integer, ForeignKey("run_table.run_id"))



    sample = relationship('Sample', back_populates='sample_run')    

    run = relationship('Run_table', back_populates='sample_run_table')   

    qid = relationship('Quality_files', back_populates="quality_files_table") 



    def __repr__(self):

        return f"({self.sample_run_id} {self.run_id} {self.sample_id})"


class Run_table(Base):

    __tablename__ = "run_table"



    run_id = Column("run_id", Integer, primary_key=True)

    run_name = Column("run_name", String)

    datetime_started = Column("datetime_started", Integer)



    sample_run_table = relationship(

        'Sample_run', back_populates="run", cascade="all, delete-orphan"

    )

        

    def __repr__(self):

        return f"({self.run_id} {self.run_name} {self.datetime_started})"



class Quality_files(Base):

    __tablename__ = "quality_files"

    quality_files_id = Column("quality_files_id", Integer, primary_key=True)
    sample_run_id = Column(Integer, ForeignKey("sample_run.sample_run_id"))
    Picard_HsMetrics_id = Column(Integer, ForeignKey("picard_hsmetrics.Picard_HsMetrics_id"))
    samtools_flagstat_id = Column(Integer, ForeignKey("samtools_flagstat.samtools_flagstat_id"))
    Picard_markduplicates_id = Column(Integer, ForeignKey("picard_markduplicates.Picard_markduplicates_id"))
    FastQC_id = Column(Integer, ForeignKey("fastQC.FastQC_id"))


    quality_files_table = relationship(
        'Sample_run', back_populates="qid"
    )

    phsid = relationship('Picard_HsMetrics', back_populates="picard_hs_table")
    stfid = relationship('samtools_flagstat', back_populates="samtools_table")
    pmdid = relationship('Picard_markduplicates', back_populates="picard_md_table")
    fqcid = relationship('FastQC', back_populates="fastqc_table")

    def __repr__(self):

        return f"({self.quality_files_id} {self.sample_run_id} {self.Picard_HsMetrics_id} {self.samtools_flagstat_id} {self.Picard_markduplicates_id} {self.FastQC_id})"


class Picard_HsMetrics(Base):

    __tablename__ = "picard_hsmetrics"

    Picard_HsMetrics_id = Column("Picard_HsMetrics_id", Integer, primary_key=True)
    Sample = Column("Sample", String)
    BAIT_SET = Column("BAIT_SET", Float)
    BAIT_TERRITORY = Column("BAIT_TERRITORY", Float)
    BAIT_DESIGN_EFFICIENCY = Column("BAIT_DESIGN_EFFICIENCY", Float)
    ON_BAIT_BASES = Column("ON_BAIT_BASES", Float)
    NEAR_BAIT_BASES = Column("NEAR_BAIT_BASES", Float)
    OFF_BAIT_BASES = Column("OFF_BAIT_BASES", Float)
    PCT_SELECTED_BASES = Column("PCT_SELECTED_BASES", Float)
    PCT_OFF_BAIT = Column("PCT_OFF_BAIT", Float)
    ON_BAIT_VS_SELECTED = Column("ON_BAIT_VS_SELECTED", Float)
    MEAN_BAIT_COVERAGE = Column("MEAN_BAIT_COVERAGE", Float)
    PCT_USABLE_BASES_ON_BAIT = Column("PCT_USABLE_BASES_ON_BAIT", Float)
    PCT_USABLE_BASES_ON_TARGET = Column("PCT_USABLE_BASES_ON_TARGET", Float)
    FOLD_ENRICHMENT = Column("FOLD_ENRICHMENT", Float)
    HS_LIBRARY_SIZE = Column("HS_LIBRARY_SIZE", Float)
    HS_PENALTY_10X = Column("HS_PENALTY_10X", Float)
    HS_PENALTY_20X = Column("HS_PENALTY_20X", Float)
    HS_PENALTY_30X = Column("HS_PENALTY_30X", Float)
    HS_PENALTY_40X = Column("HS_PENALTY_40X", Float)
    HS_PENALTY_50X = Column("HS_PENALTY_50X", Float)
    HS_PENALTY_100X = Column("HS_PENALTY_100X", Float)
    TARGET_TERRITORY = Column("TARGET_TERRITORY", Float)
    GENOME_SIZE = Column("GENOME_SIZE", Float)
    TOTAL_READS = Column("TOTAL_READS", Float)
    PF_READS = Column("PF_READS", Float)
    PF_BASES = Column("PF_BASES", Float)
    PF_UNIQUE_READS = Column("PF_UNIQUE_READS", Float)
    PF_UQ_READS_ALIGNED = Column("PF_UQ_READS_ALIGNED", Float)
    PF_BASES_ALIGNED = Column("PF_BASES_ALIGNED", Float)
    PF_UQ_BASES_ALIGNED = Column("PF_UQ_BASES_ALIGNED", Float)
    ON_TARGET_BASES = Column("ON_TARGET_BASES", Float)
    PCT_PF_READS = Column("PCT_PF_READS", Float)
    PCT_PF_UQ_READS = Column("PCT_PF_UQ_READS", Float)
    MEAN_TARGET_COVERAGE = Column("MEAN_TARGET_COVERAGE", Float)
    MEDIAN_TARGET_COVERAGE = Column("MEDIAN_TARGET_COVERAGE", Float)
    MAX_TARGET_COVERAGE = Column("MAX_TARGET_COVERAGE", Float)
    MIN_TARGET_COVERAGE = Column("MIN_TARGET_COVERAGE", Float)
    ZERO_CVG_TARGETS_PCT = Column("ZERO_CVG_TARGETS_PCT", Float)
    PCT_EXC_DUPE = Column("PCT_EXC_DUPE", Float)
    PCT_EXC_ADAPTER = Column("PCT_EXC_ADAPTER", Float)
    PCT_EXC_MAPQ = Column("PCT_EXC_MAPQ", Float)
    PCT_EXC_BASEQ = Column("PCT_EXC_BASEQ", Float)
    PCT_EXC_OVERLAP = Column("PCT_EXC_OVERLAP", Float)
    PCT_EXC_OFF_TARGET = Column("PCT_EXC_OFF_TARGET", Float)
    FOLD_80_BASE_PENALTY = Column("FOLD_80_BASE_PENALTY", Float)
    PCT_TARGET_BASES_1X = Column("PCT_TARGET_BASES_1X", Float)
    PCT_TARGET_BASES_2X = Column("PCT_TARGET_BASES_2X", Float)
    PCT_TARGET_BASES_10X = Column("PCT_TARGET_BASES_10X", Float)
    PCT_TARGET_BASES_20X = Column("PCT_TARGET_BASES_20X", Float)
    PCT_TARGET_BASES_30X = Column("PCT_TARGET_BASES_30X", Float)
    PCT_TARGET_BASES_40X = Column("PCT_TARGET_BASES_40X", Float)
    PCT_TARGET_BASES_50X = Column("PCT_TARGET_BASES_50X", Float)
    PCT_TARGET_BASES_100X = Column("PCT_TARGET_BASES_100X", Float)
    AT_DROPOUT = Column("AT_DROPOUT", Float)
    GC_DROPOUT = Column("GC_DROPOUT", Float)
    HET_SNP_SENSITIVITY = Column("HET_SNP_SENSITIVITY", Float)
    HET_SNP_Q = Column("HET_SNP_Q", Float)
    SAMPLE_LIBRARY_READ_GROUP = Column("SAMPLE_LIBRARY_READ_GROUP", Float)

# realtionship
    picard_hs_table =  relationship(
        'Quality_files', back_populates='phsid'
    )

    def __repr__(self):
        return f"({self.Picard_HsMetrics_id} {self.Sample} {self.BAIT_SET} {self.BAIT_TERRITORY} {self.BAIT_DESIGN_EFFICIENCY} {self.ON_BAIT_BASES} {self.NEAR_BAIT_BASES} \
        {self.OFF_BAIT_BASES} {self.PCT_OFF_BAIT} {self.ON_BAIT_VS_SELECTED} {self.MEAN_BAIT_COVERAGE} {self.PCT_USABLE_BASES_ON_BAIT} {self.PCT_USABLE_BASES_ON_TARGET} \
        {self.FOLD_ENRICHMENT} {self.HS_LIBRARY_SIZE} {self.HS_PENALTY_10X} {self.HS_PENALTY_20X} {self.HS_PENALTY_30X} {self.HS_PENALTY_40X} {self.HS_PENALTY_50X} \
        {self.HS_PENALTY_100X} {self.TARGET_TERRITORY} {self.GENOME_SIZE} {self.TOTAL_READS} {self.PF_READS} {self.PF_BASES} {self.PF_UNIQUE_READS} {self.PF_UQ_READS_ALIGNED} \
        {self.PF_BASES_ALIGNED} {self.MEAN_TARGET_COVERAGE} {self.MEDIAN_TARGET_COVERAGE} {self.MAX_TARGET_COVERAGE} {self.MIN_TARGET_COVERAGE} {self.ZERO_CVG_TARGETS_PCT} \
        {self.PCT_EXC_DUPE} {self.PCT_EXC_ADAPTER} {self.PCT_EXC_MAPQ} {self.PCT_EXC_BASEQ} {self.PCT_EXC_OVERLAP} {self.PCT_EXC_OFF_TARGET} {self.FOLD_80_BASE_PENALTY} \
        {self.PCT_TARGET_BASES_1X} {self.PCT_TARGET_BASES_2X} {self.PCT_TARGET_BASES_10X} {self.PCT_TARGET_BASES_20X} {self.PCT_TARGET_BASES_30X} {self.PCT_TARGET_BASES_40X} \
        {self.PCT_TARGET_BASES_50X} {self.PCT_TARGET_BASES_100X} {self.AT_DROPOUT} {self.GC_DROPOUT} {self.HET_SNP_SENSITIVITY} {self.HET_SNP_Q} {self.SAMPLE_LIBRARY_READ_GROUP}"


class samtools_flagstat(Base):
    __tablename__ = "samtools_flagstat"

    samtools_flagstat_id = Column("samtools_flagstat_id", Integer, primary_key=True)
    total_passed = Column("total_passed", Integer)
    total_failed = Column("total_failed", Integer)
    secondary_passed = Column("secondary_passed", Integer)
    secondary_failed = Column("secondary_failed", Integer)
    supplementary_passed = Column("supplementary_passed", Integer)
    supplementary_failed = Column("supplementary_failed", Integer)
    duplicates_passed = Column("duplicates_passed", Integer)
    duplicates_failed = Column("duplicates_failed", Integer)
    mapped_passed = Column("mapped_passed", Integer)
    mapped_failed = Column("mapped_failed", Integer)
    mapped_passed_pct = Column("mapped_passed_pct", Integer)
    mapped_failed_pct = Column("mapped_failed_pct", Integer)
    paired_in_sequencing_passed = Column("paired_in_sequencing_passed", Integer)
    paired_in_sequencing_failed = Column("paired_in_sequencing_failed", Integer)
    read1_passed = Column("read1_passed", Integer)
    read1_failed = Column("read1_failed", Integer)
    read2_passed = Column("read2_passed", Integer)
    read2_failed = Column("read2_failed", Integer)
    properly_paired_passed = Column("properly_paired_passed", Integer)
    properly_paired_failed = Column("properly_paired_failed", Integer)
    properly_paired_passed_pct = Column("properly_paired_passed_pct", Integer)
    properly_paired_failed_pct = Column("properly_paired_failed_pct", Integer)
    with_itself_and_mate_mapped_passed = Column("with_itself_and_mate_mapped_passed", Integer)
    with_itself_and_mate_mapped_failed = Column("with_itself_and_mate_mapped_failed", Integer)
    singletons_passed = Column("singletons_passed", Integer)
    singletons_failed = Column("singletons_failed", Integer)
    singletons_passed_pct = Column("singletons_passed", Integer)
    singletons_failed_pct = Column("singletons_failure_pct", Integer)
    with_mate_mapped_to_a_different_chr_passed = Column("with_mate_mapped_to_a_different_chr_passed", Integer)
    with_mate_mapped_to_a_different_chr_failed = Column("with_mate_mapped_to_a_different_chr_failed", Integer)
    with_mate_mapped_to_a_different_chr_mapQ5_passed = Column("with_mate_mapped_to_a_different_chr_passed", Integer)
    with_mate_mapped_to_a_different_chr_mapQ5_failed = Column("with_mate_mapped_to_a_different_chr_failed", Integer)
    flagstat_total = Column("flagstat_total", Integer)        

    #relationship
    samtools_table =  relationship(
        'Quality_files', back_populates='stfid'
    )

    def __repr__(self):
        return f"({self.samtools_flagstat_id} {self.total_passed} {self.total_failed} {self.secondary_passed} {self.secondary_failed} {self.supplementary_passed} \
        {self.supplementary_failed} {self.duplicates_passed} {self.duplicates_failed} {self.mapped_passed} {self.mapped_failed} {self.mapped_passed_pct} \
        {self.mapped_failed_pct} {self.paired_in_sequencing_passed} {self.paired_in_sequencing_failed} {self.read1_passed} {self.read1_failed} {self.read2_passed} \
        {self.read2_failed} {self.properly_paired_passed} {self.properly_paired_failed} {self.properly_paired_passed_pct} {self.properly_paired_failed_pct} \
        {self.with_itself_and_mate_mapped_passed} {self.with_itself_and_mate_mapped_failed} {self.singletons_passed} {self.singletons_failed} {self.singletons_passed_pct} \
        {self.singletons_failed_pct} {self.with_mate_mapped_to_a_different_chr_passed} {self.with_mate_mapped_to_a_different_chr_failed} \
        {self.with_mate_mapped_to_a_different_chr_mapQ5_passed} {self.with_mate_mapped_to_a_different_chr_mapQ5_failed} {self.flagstat_total}"

class Picard_markduplicates(Base):
    __tablename__ = "picard_markduplicates"

    Picard_markduplicates_id = Column("Picard_markduplicates_id", Integer, primary_key=True)
    Sample = Column("Sample", String)
    LIBRARY = Column("LIBRARY", Integer)
    UNPAIRED_READS_EXAMINED = Column("UNPAIRED_READS_EXAMINED", Integer)
    READ_PAIRS_EXAMINED = Column("READ_PAIRS_EXAMINED", Integer)
    SECONDARY_OR_SUPPLEMENTARY_RDS = Column("SECONDARY_OR_SUPPLEMENTARY_RDS", Integer)
    UNMAPPED_READS = Column("UNMAPPED_READS", Integer)
    UNPAIRED_READ_DUPLICATES = Column("UNPAIRED_READ_DUPLICATES", Integer)
    READ_PAIR_DUPLICATES = Column("READ_PAIR_DUPLICATES", Integer)
    READ_PAIR_OPTICAL_DUPLICATES = Column("READ_PAIR_OPTICAL_DUPLICATES", Integer)
    PERCENT_DUPLICATION = Column("PERCENT_DUPLICATION", Integer)
    ESTIMATED_LIBRARY_SIZE = Column("ESTIMATED_LIBRARY_SIZE", Integer)

#relationship

    picard_md_table =  relationship(
        'Quality_files', back_populates='pmdid'
    )

def __repr__(self):
        return f"({self.Picard_markduplicates_id} {self.Sample} {self.LIBRARY} {self.UNPAIRED_READS_EXAMINED} {self.READ_PAIRS_EXAMINED} {self.SECONDARY_OR_SUPPLEMENTARY_RDS} \
        {self.UNMAPPED_READS} {self.UNPAIRED_READ_DUPLICATES} {self.READ_PAIR_DUPLICATES} {self.READ_PAIR_OPTICAL_DUPLICATES} {self.PERCENT_DUPLICATION} \
        {self.ESTIMATED_LIBRARY_SIZE}" 


class FastQC(Base):
    __tablename__ = "fastQC"

    FastQC_id = Column("FastQC_id", Integer, primary_key=True)
    Filename = Column("Filename", String)
    File_type = Column("File_type", String)
    Encoding = Column("Encoding", String)
    Total_Sequences = Column("Total_Sequences", Float)
    Sequences_flagged_as_poor_quality = Column("Sequences_flagged_as_poor_quality", Integer)
    Sequence_length = Column("Sequence_length", Integer)
    GC = Column("GC", Float)
    total_deduplicated = Column("total_deduplicated", Float)
    avg_sequence_length = Column("avg_sequence_length", Float)
    basic_statistics = Column("basic_sataistics", String)
    per_base_sequence_quality = Column("per_base_sequence_quality", String)
    per_tile_sequence_quality = Column("per_tile_sequence_quality", String)
    per_sequence_quality_scores = Column("per_sequence_quality_scores", String)
    per_base_sequence_content = Column("per_base_sequence_content", String)
    per_base_sequence_gc_content = Column("per_base_sequence_gc_content", String)
    per_base_n_content = Column("per_base_n_content", String)
    sequence_length_distribution = Column("sequence_length_distribution", String)
    sequence_duplication_levels = Column("sequence_duplication_levels", String)
    overrepresented_sequences = Column("overrepresented_sequences", String)
    adapter_content = Column("adapter_content", String)

# realstionship
    fastqc_table =  relationship(
        'Quality_files', back_populates='fqcid'
    )


    def __repr__(self):
        return f"({self.FastQC_id} {self.Filename} {self.File_type} {self.Encoding} {self.Total_Sequences} {self.Sequences_flagged_as_poor_quality} \
        {self.Sequence_length} {self.GC} {self.total_deduplicated} {self.avg_sequence_length} {self.basic_statistics} {self.per_base_sequence_quality} \
        {self.per_tile_sequence_quality} {self.per_sequence_quality_scores} {self.per_base_sequence_content} {self.per_base_sequence_gc_content} \
        {self.per_base_n_content} {self.sequence_length_distribution} {self.sequence_duplication_levels} {self.overrepresented_sequences} {self.adapter_content}"


# create an empty database

engine = create_engine("sqlite:///amy_db.db", echo=True)

# create an empty database with the structure outlined above

Base.metadata.create_all(bind=engine)

# session uses engine to interact with the database



# create objects and persist

with Session(engine) as session:

    #session.add_all([sample_one, sample_two, run_one])

    session.add_all([

        Sample(sample_id="21_1234"),

        Sample(sample_id="21_5679"),

        Run_table(run_id="1", run_name="PaedOnc23_01", datetime_started='123'),

        Sample_run(sample_run_id='1',run_id="1", sample_id="21_1234"),
        
        Quality_files(quality_files_id='1', sample_run_id="1", Picard_HsMetrics_id='1', samtools_flagstat_id='1', Picard_markduplicates_id='1', FastQC_id='1'),
        
        Picard_HsMetrics(Picard_HsMetrics_id='1', Sample='Sample', BAIT_SET='1.1', BAIT_TERRITORY='1.1', BAIT_DESIGN_EFFICIENCY='1.1', ON_BAIT_BASES='1.1', NEAR_BAIT_BASES='1.1', \
                         OFF_BAIT_BASES='1.1', PCT_SELECTED_BASES='1.1', PCT_OFF_BAIT='1.1', ON_BAIT_VS_SELECTED='1.1', MEAN_BAIT_COVERAGE='1.1', PCT_USABLE_BASES_ON_BAIT='1.1',\
                         PCT_USABLE_BASES_ON_TARGET='1.1', FOLD_ENRICHMENT='1.1', HS_LIBRARY_SIZE='1.1', HS_PENALTY_10X='1.1', HS_PENALTY_20X='1.1', HS_PENALTY_30X='1.1', \
                         HS_PENALTY_40X='1.1', HS_PENALTY_50X='1.1', HS_PENALTY_100X='1.1', TARGET_TERRITORY='1.1', GENOME_SIZE='1.1', TOTAL_READS='1.1', PF_READS='1.1', \
                         PF_BASES='1.1', PF_UNIQUE_READS='1.1', PF_UQ_READS_ALIGNED='1.1', PF_BASES_ALIGNED='1.1', PF_UQ_BASES_ALIGNED='1.1', MEAN_TARGET_COVERAGE='1.1', \
                         MEDIAN_TARGET_COVERAGE='1.1', MAX_TARGET_COVERAGE='1.1', MIN_TARGET_COVERAGE='1.1', ZERO_CVG_TARGETS_PCT='1.1', PCT_EXC_DUPE='1.1', \
                         PCT_EXC_ADAPTER='1.1', PCT_EXC_MAPQ='1.1', PCT_EXC_BASEQ='1.1', PCT_EXC_OVERLAP='1.1', PCT_EXC_OFF_TARGET='1.1', FOLD_80_BASE_PENALTY='1.1', \
                         PCT_TARGET_BASES_1X='1.1', PCT_TARGET_BASES_2X='1.1', PCT_TARGET_BASES_10X='1.1', PCT_TARGET_BASES_20X='1.1', PCT_TARGET_BASES_30X='1.1', \
                         PCT_TARGET_BASES_40X='1.1', PCT_TARGET_BASES_50X='1.1', PCT_TARGET_BASES_100X='1.1', AT_DROPOUT='1.1', GC_DROPOUT='1.1', HET_SNP_SENSITIVITY='1.1', \
                         HET_SNP_Q='1.1', SAMPLE_LIBRARY_READ_GROUP='1.1'),
        
        samtools_flagstat(samtools_flagstat_id='1', total_passed='1', total_failed='1', secondary_passed='1', secondary_failed='1', supplementary_passed='1', \
                          supplementary_failed='1', duplicates_passed='1', duplicates_failed='1', mapped_passed='1', mapped_failed='1', mapped_passed_pct='1', \
                          mapped_failed_pct='1', paired_in_sequencing_passed='1', paired_in_sequencing_failed='1', read1_passed='1', read1_failed='1', read2_passed='1', \
                          read2_failed='1', properly_paired_passed='1', properly_paired_failed='1', properly_paired_passed_pct='1', properly_paired_failed_pct='1', \
                          with_itself_and_mate_mapped_passed='1', with_itself_and_mate_mapped_failed='1', singletons_passed='1', singletons_failed='1', \
                          singletons_passed_pct='1', singletons_failed_pct='1', with_mate_mapped_to_a_different_chr_passed='1', with_mate_mapped_to_a_different_chr_failed='1', \
                          with_mate_mapped_to_a_different_chr_mapQ5_passed='1', with_mate_mapped_to_a_different_chr_mapQ5_failed='1',flagstat_total='1'), 
                          
        Picard_markduplicates(Picard_markduplicates_id='1', Sample='Sample', LIBRARY='LIBRARY', UNPAIRED_READS_EXAMINED='1', READ_PAIRS_EXAMINED='1', SECONDARY_OR_SUPPLEMENTARY_RDS='1', \
                              UNMAPPED_READS='1', UNPAIRED_READ_DUPLICATES='1', READ_PAIR_DUPLICATES='1', READ_PAIR_OPTICAL_DUPLICATES='1', PERCENT_DUPLICATION='1', ESTIMATED_LIBRARY_SIZE='1'),
                              
        FastQC(FastQC_id='1', Filename='Filename', File_type='File_type', Encoding='Encoding', Total_Sequences='1.1', Sequences_flagged_as_poor_quality='1', \
               Sequence_length='1', GC='1.1', total_deduplicated='1.1', avg_sequence_length='1.1', basic_statistics='stats', per_base_sequence_quality='1', \
               per_tile_sequence_quality='1', per_sequence_quality_scores='1', per_base_sequence_content='1', per_base_sequence_gc_content='1', per_base_n_content='1', \
               sequence_length_distribution='1', sequence_duplication_levels='1', overrepresented_sequences='1', adapter_content='1')])



    session.commit()

#parsing files into df 
def parse(file):
    df = pd.read_csv(file, sep="\t")
    return df

dups = parse("/home/stpuser/test_git/somatic_ngs/somaticngs_pipeline_example_qc/PaedOnc23_12_132974_multiqc_report_data/multiqc_picard_dups.txt")
HsMetrics = parse("/home/stpuser/test_git/somatic_ngs/somaticngs_pipeline_example_qc/PaedOnc23_12_132974_multiqc_report_data/multiqc_picard_HsMetrics.txt")
flagstat = parse("/home/stpuser/test_git/somatic_ngs/somaticngs_pipeline_example_qc/PaedOnc23_12_132974_multiqc_report_data/multiqc_samtools_flagstat.txt")
fastQC = parse("/home/stpuser/test_git/somatic_ngs/somaticngs_pipeline_example_qc/PaedOnc23_12_132974_multiqc_report_data/multiqc_fastqc.txt")

#adding df to the database
#need to add extra headers that were missed previously for HSMEtrics
dups.to_sql(name='picard_markduplicates', con=engine, if_exists='append', index=False)
HsMetrics.to_sql(name='picard_hsmetrics', con=engine, if_exists='append', index=False)